#!/usr/bin/env python3
"""Search the catalog offline: Python 3.10+, no packages or API keys."""
import argparse
import json
from catalog_lib import CatalogError, load_catalog, select, stats


def main():
    try:
        apps, categories, features = load_catalog()
        parser = argparse.ArgumentParser(description=__doc__)
        parser.add_argument('query', nargs='?', default='', help='Case-insensitive words in name, description or category')
        parser.add_argument('--feature', action='append', default=[], choices=features, help='Repeat to require all selected features')
        parser.add_argument('--availability', choices=['available', 'source-build', 'prototype', 'beta', 'announced', 'unconfirmed'])
        parser.add_argument('--category', choices=[c['name'] for c in categories])
        parser.add_argument('--json', action='store_true', help='Emit complete records as JSON')
        parser.add_argument('--stats', action='store_true', help='Print summary counts for the current selection')
        args = parser.parse_args()
        matches = select(apps, args.query, args.feature, args.availability, args.category)
        if args.stats:
            print(json.dumps(stats(matches) if matches else {'entries': 0}, indent=2))
        elif args.json:
            print(json.dumps(matches, ensure_ascii=False, indent=2))
        else:
            print(f'{len(matches)} matches')
            for a in matches:
                print(f'\n{a["name"]} [{a["availability"]}; {a["tier"]}]\n  {a["description"]}\n  {a["url"]}')
    except CatalogError as error:
        raise SystemExit(str(error)) from error


if __name__ == '__main__':
    main()
