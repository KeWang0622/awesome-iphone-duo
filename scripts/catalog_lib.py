"""Shared, dependency-free catalog validation and querying helpers."""
from collections import Counter
from datetime import date
import ipaddress
import json
from pathlib import Path
import re
from urllib.parse import parse_qsl, unquote, urlsplit, urlunsplit

ROOT = Path(__file__).resolve().parents[1]


class CatalogError(ValueError):
    pass


def require(condition, message):
    if not condition:
        raise CatalogError(message)


def read_json(path):
    def unique_keys(pairs):
        result = {}
        for key, value in pairs:
            require(key not in result, f'{path}: duplicate JSON key {key}')
            result[key] = value
        return result
    try:
        return json.loads(Path(path).read_text(), object_pairs_hook=unique_keys)
    except (OSError, json.JSONDecodeError) as error:
        raise CatalogError(f'{path}: {error}') from error


def validate_structure(value, schema, path='catalog'):
    """Validate the JSON Schema keywords used by this repository's schemas.

    This is deliberately not a general JSON Schema implementation. Unsupported
    validation keywords fail closed rather than silently accepting records.
    """
    supported = {'$schema', '$id', 'title', 'description', 'type', 'properties',
                 'required', 'additionalProperties', 'items', 'minItems',
                 'uniqueItems', 'minLength', 'maxLength', 'pattern', 'enum'}
    require(not (set(schema) - supported), f'{path}: unsupported schema keywords {set(schema) - supported}')
    types = {'object': dict, 'array': list, 'string': str, 'boolean': bool}
    if 'type' in schema:
        require(type(value) is types[schema['type']], f'{path}: expected {schema["type"]}')
    if 'enum' in schema:
        require(value in schema['enum'], f'{path}: unknown value {value!r}')
    if isinstance(value, str):
        require(len(value) >= schema.get('minLength', 0), f'{path}: empty string')
        require(len(value) <= schema.get('maxLength', len(value)), f'{path}: too long')
        if 'pattern' in schema:
            require(re.search(schema['pattern'], value), f'{path}: invalid format')
    if isinstance(value, list):
        require(len(value) >= schema.get('minItems', 0), f'{path}: not enough entries')
        if schema.get('uniqueItems'):
            require(len({json.dumps(v, sort_keys=True) for v in value}) == len(value), f'{path}: duplicate items')
        for i, item in enumerate(value):
            if 'items' in schema:
                validate_structure(item, schema['items'], f'{path}[{i}]')
    if isinstance(value, dict):
        require(set(schema.get('required', [])) <= value.keys(), f'{path}: missing required fields {set(schema.get("required", [])) - value.keys()}')
        properties = schema.get('properties', {})
        extra = schema.get('additionalProperties', True)
        for key, item in value.items():
            if key in properties:
                validate_structure(item, properties[key], f'{path}.{key}')
            elif isinstance(extra, dict):
                validate_structure(item, extra, f'{path}.{key}')
            else:
                require(extra is not False, f'{path}: unknown field {key}')


def public_url(value):
    require(isinstance(value, str) and not re.search(r'[\s<>"\\()]', value), f'Unsafe URL: {value!r}')
    try:
        p = urlsplit(value)
        host = (p.hostname or '').rstrip('.')
        require(p.scheme == 'https' and host and not p.username and not p.password, f'Expected public HTTPS URL: {value}')
        require(p.port in {None, 443}, f'Unexpected URL port: {value}')
        require('.' in host and host != 'localhost' and not host.endswith(('.local', '.localhost', '.internal')), f'Non-public host: {value}')
        try:
            address = ipaddress.ip_address(host)
        except ValueError:
            address = None
        require(address is None or address.is_global, f'Non-public IP: {value}')
        if address is None:
            labels = host.split('.')
            require(all(re.fullmatch(r'[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?', label, re.I) for label in labels), f'Invalid hostname: {value}')
            require(re.search(r'[a-z]', labels[-1], re.I), f'Non-public numeric host: {value}')
        for key, _ in parse_qsl(p.query):
            require(not key.lower().startswith('utm_') and key.lower() not in {'afid', 'affiliate', 'ct', 'pt'}, f'Tracking URL: {value}')
    except ValueError as error:
        if isinstance(error, CatalogError):
            raise
        raise CatalogError(f'Malformed URL: {value}') from error
    return p


def canonical_url(value):
    """Catch the same app across App Store countries, slugs, or query strings."""
    p = public_url(value)
    host = p.hostname.lower().removeprefix('www.')
    if host == 'apps.apple.com':
        app_id = re.search(r'/id(\d+)(?:/|$)', p.path)
        if app_id:
            return f'appstore:{app_id.group(1)}'
    path = unquote(p.path).rstrip('/') or '/'
    if host == 'github.com':
        path = path.lower().removesuffix('.git')
    return urlunsplit(('https', host, path, p.query, ''))


def anchor(text):
    text = re.sub(r'\[([^\]]+)\]\([^)]*\)', r'\1', text)
    return re.sub(r'[^\w\- ]', '', text.lower()).replace(' ', '-')


def validate_catalog(apps, categories, features, schema, today=None):
    today = today or date.today()
    validate_structure(apps, schema)
    names = {c['name'] for c in categories}
    require(len(names) == len(categories), 'Duplicate category')
    require(len({c['id'] for c in categories}) == len(categories), 'Duplicate category ID')
    for c in categories:
        require(anchor(c['name']) == c['id'], f'Invalid category anchor: {c["name"]}')
        require(any(a['category'] == c['name'] for a in apps), f'Empty category: {c["name"]}')
    seen = {key: set() for key in ('id', 'name', 'url')}
    for app in apps:
        name = app['name']
        for key in seen:
            v = canonical_url(app[key]) if key == 'url' else app[key].casefold()
            require(v not in seen[key], f'Duplicate {key}: {app[key]}')
            seen[key].add(v)
        require(app['category'] in names, f'{name}: unknown category')
        require(app['description'].endswith('.'), f'{name}: description must end with a period')
        for field in ('name', 'description', 'limitation'):
            require(not re.search(r'[\n\r<>\[\]|]', app.get(field, '')), f'{name}: unsafe Markdown in {field}')
        try:
            checked = date.fromisoformat(app['checked_at'])
        except ValueError as error:
            raise CatalogError(f'{name}: invalid check date') from error
        require(checked <= today, f'{name}: future source-check date')
        for field in ('url', 'evidence_url', 'source_url'):
            if field in app:
                public_url(app[field])
        for url in app.get('additional_evidence_urls', []):
            public_url(url)
        require(set(app['features']) <= features.keys(), f'{name}: unknown feature')
        require(set(app['feature_evidence']) == set(app['features']), f'{name}: each feature needs exactly one evidence URL')
        for url in app['feature_evidence'].values():
            public_url(url)
        require('support-only' not in app['features'] or len(app['features']) == 1, f'{name}: support-only cannot coexist with specific features')
        expected = {'source-build': 'Source projects and experiments', 'prototype': 'Source projects and experiments', 'beta': 'Previews and watchlist', 'announced': 'Previews and watchlist', 'unconfirmed': 'Previews and watchlist'}
        if app['availability'] in expected:
            require(app['category'] == expected[app['availability']], f'{name}: availability/category mismatch')
        else:
            require(app['category'] not in set(expected.values()), f'{name}: available app in preview/experiment category')
    order = {c['name']: i for i, c in enumerate(categories)}
    require(apps == sorted(apps, key=lambda a: (order[a['category']], a['name'].casefold())), 'Sort apps by category order, then name')


def load_catalog(root=ROOT):
    apps = read_json(root / 'data/apps.json')
    categories = read_json(root / 'data/categories.json')
    features = read_json(root / 'data/features.json')
    schema = read_json(root / 'data/catalog.schema.json')
    validate_catalog(apps, categories, features, schema)
    return apps, categories, features


def select(apps, text='', features=(), availability=None, category=None):
    words = text.casefold().split()
    return [a for a in apps
            if all(word in ' '.join((a['name'], a['description'], a['category'])).casefold() for word in words)
            and set(features) <= set(a['features'])
            and (availability is None or a['availability'] == availability)
            and (category is None or a['category'] == category)]


def stats(apps):
    return {'entries': len(apps), 'availability': dict(sorted(Counter(a['availability'] for a in apps).items())),
            'evidence': dict(sorted(Counter(a['tier'] for a in apps).items())),
            'features': dict(sorted(Counter(f for a in apps for f in a['features']).items())),
            'latest_source_review': max(a['checked_at'] for a in apps)}
