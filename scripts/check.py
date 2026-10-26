#!/usr/bin/env python3
"""Validate source data, generated files, test reports, and local Markdown links."""
from collections import Counter
from datetime import date
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit
from build_readme import generated_files
from catalog_lib import ROOT, CatalogError, anchor, load_catalog, public_url, read_json, require, validate_structure


def validate_reports(reports, apps, schema, today=None):
    validate_structure(reports,schema,'test reports')
    today=today or date.today()
    ids={a['id'] for a in apps}
    seen=set()
    for report in reports:
        require(report['id'] not in seen,'Duplicate test report ID')
        seen.add(report['id'])
        require(report['app_id'] in ids,'Test report refers to unknown app')
        require(date.fromisoformat(report['tested_at'])<=today,'Future hands-on test date')
        public_url(report['evidence_url'])


def without_code_fences(text):
    lines = []
    fence = None
    for line in text.splitlines():
        marker = re.match(r'^ {0,3}(`{3,}|~{3,})(.*)$', line)
        if fence:
            if marker and marker[1][0] == fence[0] and len(marker[1]) >= len(fence) and not marker[2].strip():
                fence = None
        elif marker:
            fence = marker[1]
        else:
            lines.append(line)
    return '\n'.join(lines)


def markdown_anchors(text):
    text = without_code_fences(text)
    found=set(re.findall(r'<a id="([^"]+)"',text))
    seen=Counter()
    for heading in re.findall(r'^#{1,6} (.+)$',text,re.M):
        slug=anchor(heading)
        found.add(slug if seen[slug]==0 else f'{slug}-{seen[slug]}')
        seen[slug]+=1
    return found


def check_markdown(root=ROOT):
    for path in root.rglob('*.md'):
        if '.git' in path.parts or path.name in {'readme-intro.md','readme-outro.md'}:
            continue  # fragments are checked in their generated README context
        text=without_code_fences(path.read_text())
        require('\t' not in text,f'Tab character: {path}')
        definitions = dict((key.strip().casefold(), value) for key, value in re.findall(r'^ {0,3}\[([^\]]+)\]:\s*<?([^\s>]+)>?',text,re.M))
        destinations = re.findall(r'\]\(([^)\s]+)\)',text)
        destinations.extend(definitions.values())
        for label, reference in re.findall(r'\[([^\]]+)\]\[([^\]]*)\]', text):
            key = (reference or label).strip().casefold()
            require(key in definitions, f'Undefined Markdown reference in {path.name}: {key}')
        for destination in destinations:
            if urlsplit(destination).scheme or destination.startswith('//'):
                continue
            filename,_,fragment=unquote(destination).partition('#')
            target=(path.parent/filename).resolve() if filename else path.resolve()
            require(target.is_relative_to(root.resolve()),f'Local link leaves repository: {destination}')
            require(target.exists(),f'Broken link in {path.name}: {destination}')
            if fragment and target.suffix=='.md':
                require(fragment in markdown_anchors(target.read_text()),f'Broken anchor in {path.name}: {destination}')


def main():
    try:
        apps,categories,_=load_catalog()
        validate_reports(read_json(ROOT/'data/test-reports.json'),apps,read_json(ROOT/'data/test-report.schema.json'))
        for name,expected in generated_files().items():
            require((ROOT/name).read_text()==expected,f'{name} is stale; run python3 scripts/build_readme.py')
        check_markdown()
        print(f'OK: {len(apps)} unique apps, {len(categories)} categories, schema, canonical identities, feature evidence, dates, generated files, test records and local links.')
    except (CatalogError,OSError,ValueError) as error:
        raise SystemExit(str(error)) from error


if __name__=='__main__':
    main()
