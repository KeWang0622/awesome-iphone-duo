#!/usr/bin/env python3
"""Build README, interaction index and summary from the checked catalog."""
import json
from catalog_lib import ROOT, load_catalog, read_json, stats

LABELS = {'primary': 'Primary', 'curated': 'Apple collection', 'reported': 'Reported', 'community': 'Community'}
STATUS = {'available': 'Available', 'source-build': 'Build from source', 'prototype': 'Prototype', 'beta': 'Beta', 'announced': 'Announced', 'unconfirmed': 'Unconfirmed'}


def app_link(app, prefix=''):
    return f'[{app["name"]}]({prefix}README.md#app-{app["id"]})'


def render(apps=None, categories=None):
    if apps is None:
        apps, categories, _ = load_catalog()
    info = stats(apps)
    intro = (ROOT / 'docs/readme-intro.md').read_text().rstrip()
    intro = intro.replace('{{COUNT}}', str(len(apps))).replace('{{REVIEW_DATE}}', info['latest_source_review'])
    intro = intro.replace('{{AVAILABLE}}', str(info['availability'].get('available', 0)))
    intro = intro.replace('{{SOURCE_BUILD}}', str(info['availability'].get('source-build', 0)))
    intro = intro.replace('{{PROTOTYPES}}', str(info['availability'].get('prototype', 0)))
    previews = sum(info['availability'].get(k, 0) for k in ('announced', 'beta', 'unconfirmed'))
    intro = intro.replace('{{PREVIEWS}}', str(previews))
    contents = '## Contents\n\n' + '\n'.join(f'- [{c["name"]}](#{c["id"]})' for c in categories)
    contents += '\n- [References and related lists](#references-and-related-lists)\n- [Contributing](#contributing)'
    sections = [intro, contents]
    for c in categories:
        entries = [a for a in apps if a['category'] == c['name']]
        lines = []
        for a in entries:
            tags = [f'[{LABELS[a["tier"]]}]({a["evidence_url"]})']
            tags.extend(f'[Details]({url})' for url in a.get('additional_evidence_urls', []))
            if a['availability'] != 'available':
                tags.append(STATUS[a['availability']])
            if a.get('source_url'):
                tags.append(f'[Source]({a["source_url"]})')
            entry = f'- <a id="app-{a["id"]}"></a>[{a["name"]}]({a["url"]}) - {a["description"]} ' + ' · '.join(tags) + '.'
            if a.get('limitation'):
                entry += f' **Needs / limits:** {a["limitation"]}'
            lines.append(entry)
        sections.append(f'## {c["name"]}\n\n{c["description"]}\n\n' + '\n'.join(lines))
    sections.append((ROOT / 'docs/readme-outro.md').read_text().strip())
    return '\n\n'.join(sections) + '\n'


def render_interactions(apps, features):
    out = ['# Find an app by interaction',
           'Every tag below has a source URL in `feature_evidence` in the [catalog](../data/apps.json). Tags describe the reviewed evidence; an absent tag does not prove a feature is unsupported. Availability is shown separately.',
           '**Installable apps and prototypes appear in separate groups.** The cover-screen tag does not imply simultaneous use of both displays.',
           ' | '.join(f'[{v["label"]}](#{k})' for k,v in features.items())]
    for feature, meta in features.items():
        out.append(f'<a id="{feature}"></a>\n\n## {meta["label"]}\n\n{meta["description"]}')
        for released, title in [(True, 'Available apps'), (False, 'Source projects and previews')]:
            selected = sorted((a for a in apps if feature in a['features'] and (a['availability']=='available') == released), key=lambda a:a['name'].casefold())
            if not selected:
                continue
            lines = [f'### {title}', '| App | Access | Feature evidence |', '| --- | --- | --- |']
            lines.extend(f'| {app_link(a, "../")} | {STATUS[a["availability"]]} | [{LABELS[a["tier"]]}]({a["feature_evidence"][feature]}) |' for a in selected)
            out.append(lines[0]+'\n\n'+'\n'.join(lines[1:]))
    out.append('## Search offline\n\nUse the [Python command](tooling.md) to combine features, availability and search terms. No account, network request or extra packages are needed.')
    return '\n\n'.join(out)+'\n'


def generated_files():
    apps,categories,features=load_catalog()
    reports=read_json(ROOT/'data/test-reports.json')
    summary=stats(apps)
    summary['categories']=len(categories)
    summary['accepted_physical_device_reports']=sum(r['environment']=='physical-device' for r in reports)
    summary['accepted_simulator_reports']=sum(r['environment']=='simulator' for r in reports)
    return {'README.md':render(apps,categories),
            'docs/interaction-index.md':render_interactions(apps,features),
            'reports/catalog-summary.json':json.dumps(summary,indent=2)+'\n'}


if __name__ == '__main__':
    for name, content in generated_files().items():
        (ROOT/name).parent.mkdir(parents=True,exist_ok=True)
        (ROOT/name).write_text(content)
        print(f'Generated {name}')
