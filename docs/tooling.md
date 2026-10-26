# Search and maintain the catalog

Python 3.10 or newer is sufficient. The catalog, search command and local checks need no packages, API key or network connection. Run commands from the repository root.

## Find an app

```sh
# Available apps that use the hinge as a control
python3 scripts/catalog.py --feature hinge-input --availability available

# Require both hinge input and a cover-screen experience
python3 scripts/catalog.py --feature hinge-input --feature cover-display

# Match every word, ignoring case
python3 scripts/catalog.py "remote Mac"

# Export full matching records, including evidence and limitations
python3 scripts/catalog.py --category "Music and instruments" --json

# Counts for any selection
python3 scripts/catalog.py --availability prototype --stats
```

Feature filters intersect: repeating `--feature` requires **all** selected features. Text searches names, descriptions and categories. No results produce an empty list, not an error. See `--help` for valid category, feature and access values.

The [interaction index](interaction-index.md) offers the same feature groups without a terminal. Missing tags mean evidence has not been recorded, not that a feature is absent.

## Make a change

1. Edit [data/apps.json](../data/apps.json), preserving stable IDs and category order. Follow [CONTRIBUTING](../CONTRIBUTING.md).
2. Rebuild the generated files.
3. Run integrity checks and regression tests.

```sh
python3 scripts/build_readme.py
python3 scripts/check.py
python3 -m unittest discover -s tests -v
```

Or use `make build` and `make verify`. CI runs checks and tests on Python 3.10 and 3.13.

## Source files and generated files

| File | Purpose |
| --- | --- |
| [data/apps.json](../data/apps.json) | App identity, original description, evidence, access, feature-specific sources and source-review date. |
| [data/catalog.schema.json](../data/catalog.schema.json) | Machine-readable record structure and allowed values. |
| [data/categories.json](../data/categories.json) | Category order and introductions. |
| [data/features.json](../data/features.json) | Exact feature definitions. |
| [data/test-reports.json](../data/test-reports.json) | Reviewed contributor observations; currently empty. |
| [README introduction](readme-intro.md) / [ending](readme-outro.md) | Editable prose surrounding the generated app lists. |
| [README](../README.md), [interaction index](interaction-index.md), [catalog summary](../reports/catalog-summary.json) | Generated outputs; do not edit directly. |

## What the checks establish

The checks reject duplicate app names, stable IDs and canonical download URLs, including the same App Store ID in different countries. They validate required fields, allowed values, availability/category consistency, per-feature evidence coverage, dates, local links and generated-file freshness. Regression tests exercise failure cases as well as search behavior.

The standard JSON schemas can be used by other tools. Our dependency-free validator implements only their documented subset of schema keywords and rejects unsupported keywords. It is not a general JSON Schema engine.

Automation does **not** read source pages to prove claims, resolve every URL to a public server, test devices, assess licenses or certify app quality. Review evidence manually; a successful HTTP response would not prove that a linked page still supports a claim. A blocked or timed-out request is not proof an app disappeared. Never refresh `checked_at` merely because a script ran.
