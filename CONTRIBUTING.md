# Contributing

Help people find something worth doing with an iPhone Duo. Small indie apps, paid apps and open-source experiments are welcome.

## Suggest an app

Open an app suggestion issue or edit `data/apps.json` in a pull request. One app per suggestion makes review easier.

Include:

- A direct developer, App Store or source-repository URL, without tracking or affiliate parameters.
- An original, short description of what the app does and why the Duo matters.
- A public evidence URL explicitly supporting Duo behavior or inclusion in an Apple Duo collection.
- Availability: `available`, `source-build`, `prototype`, `beta`, `announced`, or `unconfirmed`.
- Evidence: `primary`, `curated`, `reported`, or `community`.
- Feature tags from [data/features.json](data/features.json), with one supporting URL for every tag in `feature_evidence`. Use `support-only` alone when the source documents Duo support but no specific interaction.
- The source-check date as `YYYY-MM-DD` and a brief evidence note, preferably naming the app version.
- Any host computer, accessory, subscription or build requirement material to the described use.
- Your relationship to the app, if you make it, work for it, or receive compensation.

Use `primary` for explicit developer, official platform announcement, App Store release-note or source-repository evidence; `curated` for an Apple Duo collection without a documented special layout; `reported` for independent editorial coverage; and `community` for user reports. Availability and evidence are separate: a developer's prototype can have primary evidence without being released.

Do not infer Duo optimization from iPad support, an ordinary iPhone compatibility line, a mockup, or a search snippet that you have not checked. A general iPhone app needs a specific, documented reason to appear here. Keep previews and source-build experiments in their designated categories. Use `prototype` for a demo or research submission whose build and release availability is not established; do not infer a working build from a repository link. Avoid duplicate listings, superlatives, copied marketing text, unsupported privacy promises, fixed prices, and popularity thresholds.

## Edit and check

Use Python 3.10 or newer; no additional packages are required.

```sh
python3 scripts/build_readme.py
python3 scripts/check.py
python3 -m unittest discover -s tests -v
```

`data/apps.json` contains entries, `data/categories.json` controls their grouping, and `docs/readme-intro.md` / `docs/readme-outro.md` contain the surrounding prose. The README, interaction index and summary report are generated; edit the sources instead. See [tooling](docs/tooling.md) for search commands and the [catalog schema](data/catalog.schema.json) for record fields. Keep a unique stable `id` for each app, and alphabetize entries within categories. `source_url` is optional and means the actual app source is available, not merely a release-download repository.

## Corrections and hands-on reports

Report renamed apps, discontinued downloads, unsupported features or inaccurate links with the correction issue template. A blocked HTTP request is not proof that an app is gone. Prefer a replacement official source before removal.

This list began with AI-assisted web research. Source checking is not device testing. Use the [test-report protocol](docs/testing.md) for observations: it requires device, environment, OS and app versions, steps, date, result and evidence. Physical-device and simulator reports stay distinct. Never add an unqualified “tested” claim.

Be respectful, focus feedback on the entry, and do not share credentials or private logs. Contributions to original repository content are offered under [CC0](LICENSE); linked apps retain their own licenses.
