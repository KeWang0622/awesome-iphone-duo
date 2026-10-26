# Research and curation

Initial research date: **October 26, 2026**. This catalog began with AI-assisted web research. We checked published sources; we did not install these apps or test them on an iPhone Duo. Descriptions summarize documented behavior, not our experience or a guarantee of compatibility.

## What belongs here

The focus is interesting things people can do with iPhone Duo: use a pocket workstation, play with hinge controls, make music, read, create, and arrange useful tools across the larger display. Ordinary iPhone compatibility or an iPad version is insufficient evidence of Duo adaptation.

We favor a concrete use over promotional claims. Every app needs a public supporting reference, an original description, and a source-check date. Small projects and paid apps can be useful; popularity is not an admission requirement. Download and pricing details can change, so follow the developer's current instructions.

## Evidence and availability are separate

The `tier` field describes where a claim comes from:

| Tier | Meaning |
| --- | --- |
| `primary` | Explicit developer documentation, App Store text, release notes, or the project's source repository supports the Duo claim. |
| `curated` | Apple includes the app in a Duo collection, without necessarily documenting a special interaction. |
| `reported` | Independent editorial coverage describes Duo support or behavior. |
| `community` | A public user report supplies the evidence. |

The `availability` field describes access: `available`, `source-build`, `prototype`, `beta`, `announced`, or `unconfirmed`. A prototype can have primary evidence without having an installable release or a verified build. A store app can be available while its Duo behavior is supported only by a report. Neither field means we tested it.

Entries preserve an `evidence_url`, an explanatory note, and `checked_at`. The date records a source review, not the app's release date. A `source_url` points to app source code; availability of code alone does not establish an open-source license. Each feature has its own evidence URL; a source that supports a pose layout does not automatically establish hinge input or system Split View. [Test reports](testing.md) separately name the environment, device, OS and app versions, steps, date, observed behavior and limitations.

## Repository design

The [Awesome manifesto](https://github.com/sindresorhus/awesome/blob/main/awesome.md) informed the focused scope, useful descriptions, contribution guidance, and CC0 content license. [Awesome Mac](https://github.com/jaywcjlove/awesome-mac) demonstrates categories organized around practical tasks and a short link legend. [Awesome iOS](https://github.com/vsouza/awesome-ios) is a complementary developer reference, not a substitute for consumer app discovery.

The README uses compact category lists for readability on a phone. Structured records make dates, evidence, duplicate checks, and README regeneration manageable; [Open-Source iOS Apps](https://github.com/dkhamsing/open-source-ios-apps) offers a mature example of that approach. Keeping source-build experiments and previews separate makes access requirements visible without discarding interesting ideas.

An existing [awesome-iphone-duo](https://github.com/mergisi/awesome-iphone-duo) focuses on development resources. Our emphasis is applications and practical uses; we link related work rather than claiming to be the first Duo list. [FoldHunt](https://foldhunt.com/) is another discovery source; its listings are leads to inspect, not substitutes for each entry's cited evidence.

The broader [landscape review](landscape.md) compares ten directories and repositories. Several already offer feature filters, evidence or guides. This project combines a forkable dataset, inspectable per-feature sources, task recipes and dependency-free local checks; we make no claim of exclusive features or internet-wide uniqueness.

## Independence and maintenance

The Awesome badge is permitted on independent lists; it does not mean inclusion in or endorsement by the central directory. That directory's current [submission requirements](https://github.com/sindresorhus/awesome/blob/main/pull_request_template.md) include a minimum age of 30 days and a non-AI-generated list. This AI-assisted catalog makes no submission or eligibility claim.

[Awesome lint](https://github.com/sindresorhus/awesome-lint) is a useful formatting reference. Repository checks validate structure and links within the repository; passing them does not establish app quality, live external-link availability, or compatibility. Report corrections through the contribution process. Review blocked requests before removing an entry: a network error alone does not show that an app has disappeared.
