"""Regression tests for integrity rules that protect the public catalog."""
import copy
from datetime import date
import json
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from catalog_lib import ROOT, CatalogError, canonical_url, load_catalog, public_url, read_json, select, validate_catalog
from check import check_markdown, validate_reports

TODAY=date.today()


class CatalogTests(unittest.TestCase):
    def setUp(self):
        self.apps,self.categories,self.features=load_catalog()
        self.schema=read_json(ROOT/'data/catalog.schema.json')

    def check(self,apps):
        validate_catalog(apps,self.categories,self.features,self.schema,today=TODAY)

    def test_app_store_regions_and_slugs_have_one_identity(self):
        first='https://apps.apple.com/us/app/example/id12345'
        second='https://apps.apple.com/jp/app/another-name/id12345?platform=ipad'
        self.assertEqual(canonical_url(first),canonical_url(second))

    def test_duplicate_app_store_id_rejected(self):
        apps=copy.deepcopy(self.apps)
        stores=[a for a in apps if 'apps.apple.com' in a['url']]
        appid=canonical_url(stores[0]['url']).split(':')[1]
        stores[1]['url']=f'https://apps.apple.com/fr/app/renamed/id{appid}'
        with self.assertRaisesRegex(CatalogError,'Duplicate url'):
            self.check(apps)

    def test_missing_feature_evidence_rejected(self):
        apps=copy.deepcopy(self.apps)
        apps[0]['feature_evidence']={}
        with self.assertRaisesRegex(CatalogError,'each feature'):
            self.check(apps)

    def test_support_only_cannot_claim_specific_feature(self):
        apps=copy.deepcopy(self.apps)
        apps[0]['features'].append('support-only')
        apps[0]['feature_evidence']['support-only']=apps[0]['evidence_url']
        with self.assertRaisesRegex(CatalogError,'cannot coexist'):
            self.check(apps)

    def test_preview_cannot_appear_among_released_apps(self):
        apps=copy.deepcopy(self.apps)
        apps[0]['availability']='beta'
        with self.assertRaisesRegex(CatalogError,'availability/category'):
            self.check(apps)

    def test_future_review_rejected(self):
        apps=copy.deepcopy(self.apps)
        apps[0]['checked_at']='2099-01-01'
        with self.assertRaisesRegex(CatalogError,'future'):
            self.check(apps)

    def test_unknown_field_rejected(self):
        apps=copy.deepcopy(self.apps)
        apps[0]['avaialability']='available'
        with self.assertRaisesRegex(CatalogError,'unknown field'):
            self.check(apps)

    def test_unsafe_markdown_rejected(self):
        apps=copy.deepcopy(self.apps)
        apps[0]['description']='A description.\n<script>bad</script>.'
        with self.assertRaisesRegex(CatalogError,'unsafe Markdown'):
            self.check(apps)

    def test_public_url_policy(self):
        for url in ['http://example.com','https://user:secret@example.com','https://127.0.0.1/a','https://127.0.0.1./a','https://127.1/a','https://example..com','https://example.com/a)b','https://localhost/a','https://example.com\n/b','https://example.com/?utm_source=x']:
            with self.subTest(url=url), self.assertRaises(CatalogError):
                public_url(url)
        public_url('https://developer.apple.com/news/?id=example')

    def test_duplicate_json_keys_rejected(self):
        with tempfile.TemporaryDirectory() as folder:
            path=Path(folder)/'bad.json'
            path.write_text('{"name":"one","name":"two"}')
            with self.assertRaisesRegex(CatalogError,'duplicate JSON key'):
                read_json(path)

    def test_filter_intersection_not_union(self):
        selected=select(self.apps,features=['hinge-input','cover-display'],availability='available')
        self.assertTrue(selected)
        self.assertTrue(all({'hinge-input','cover-display'}<=set(a['features']) and a['availability']=='available' for a in selected))
        self.assertEqual(select(self.apps,'THIS-APP-DOES-NOT-EXIST'),[])

    def test_search_matches_all_words_case_insensitively(self):
        matches=select(self.apps,'REMOTE MAC')
        self.assertTrue(matches)
        self.assertTrue(all('remote' in (a['name']+' '+a['description']+' '+a['category']).lower() and 'mac' in (a['name']+' '+a['description']+' '+a['category']).lower() for a in matches))

    def test_local_anchor_checked_and_escape_rejected(self):
        with tempfile.TemporaryDirectory() as folder:
            root=Path(folder)
            (root/'README.md').write_text('<a id="app-test"></a>\n[go](#app-test)\n')
            check_markdown(root)
            (root/'README.md').write_text('[broken](#missing)\n')
            with self.assertRaisesRegex(CatalogError,'Broken anchor'):
                check_markdown(root)
            (root/'README.md').write_text('[escape](../outside.md)\n')
            with self.assertRaisesRegex(CatalogError,'leaves repository'):
                check_markdown(root)

    def test_test_report_requires_known_app_and_context(self):
        schema=read_json(ROOT/'data/test-report.schema.json')
        report={key:'example' for key in schema['items']['required']}
        report.update(id='example-report',app_id=self.apps[0]['id'],environment='physical-device',tested_at='2026-10-26',result='partial',steps=['Open the app.'],evidence_url='https://github.com/example/repo/issues/1')
        validate_reports([report],self.apps,schema,today=TODAY)
        report['app_id']='unknown-app'
        with self.assertRaisesRegex(CatalogError,'unknown app'):
            validate_reports([report],self.apps,schema,today=TODAY)

    def test_reference_links_and_code_sample_headings(self):
        with tempfile.TemporaryDirectory() as folder:
            root=Path(folder)
            page=root/'README.md'
            page.write_text('[broken][ref]\n\n[ref]: missing.md\n')
            with self.assertRaisesRegex(CatalogError,'Broken link'):
                check_markdown(root)
            page.write_text('[broken][missing]\n')
            with self.assertRaisesRegex(CatalogError,'Undefined Markdown reference'):
                check_markdown(root)
            page.write_text('[go](#imaginary)\n\n```md\n# Imaginary\n```\n')
            with self.assertRaisesRegex(CatalogError,'Broken anchor'):
                check_markdown(root)
            page.write_text('# Real\n[go][real]\n\n[real]: #real\n\n~~~md\n[example](missing.md)\n~~~\n')
            check_markdown(root)

    def test_report_environment_must_be_explicit(self):
        schema=read_json(ROOT/'data/test-report.schema.json')
        report={key:'example' for key in schema['items']['required']}
        report.update(id='example-report',app_id=self.apps[0]['id'],tested_at=TODAY.isoformat(),result='passed',steps=['Open the app.'],evidence_url='https://github.com/example/repo/issues/1')
        with self.assertRaisesRegex(CatalogError,'unknown value'):
            validate_reports([report],self.apps,schema,today=TODAY)
        report['environment']='simulator'
        validate_reports([report],self.apps,schema,today=TODAY)


if __name__=='__main__':
    unittest.main()
