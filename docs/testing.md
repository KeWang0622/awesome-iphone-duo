# Contribute a reproducible test

Source review and device testing answer different questions. This project currently has **zero accepted test reports**. Do not interpret a source citation, CI badge or simulator screenshot as a hardware test.

Use the [hands-on report form](https://github.com/KeWang0622/awesome-iphone-duo/issues/new?template=hands-on-report.yml) or submit a record in [data/test-reports.json](../data/test-reports.json). One report describes one app, version and setup. Reports are contributor observations, not certification of every feature.

## A useful test session

1. Record the app's catalog ID, app version, iOS version, device model, test date and whether you used physical hardware or a simulator. Include required host OS, accessories, account plan and network arrangement in the steps.
2. Choose one documented behavior. Start from a reproducible state and describe the exact actions. For a pose layout, check fully open, partially folded and closed states, then reopen. For hinge input, test the action and whether it pauses or resets appropriately.
3. Record what actually happened: layout, input response, continuity and any failure. For remote desktops, separate connection trouble from fold-layout trouble. Record timing only if you measured it and describe the method.
4. Include a public issue, video or screenshot reference with personal content removed. Say which claims you did not test. Simulator results belong in their own environment field.

Use `passed` if the specified behavior worked, `partial` if some described steps failed or remained untested, and `failed` if the target behavior did not work. A narrow passing report does not mean the entire app passed.

## Record format

The [report schema](../data/test-report.schema.json) requires:

| Field | Record |
| --- | --- |
| `id`, `app_id` | Unique report ID and existing catalog app ID. |
| `tester` | Public contributor handle. |
| `environment` | `physical-device` or `simulator`. |
| `device`, `os_version`, `app_version` | Specific model or simulator target, OS and app versions. |
| `tested_at`, `result` | ISO date and `passed`, `partial` or `failed`. |
| `steps` | Ordered actions, including setup dependencies. |
| `observed` | Actual result, failures and limits. |
| `evidence_url` | Public link supporting the report. |

Maintainers review the evidence before accepting a report. The scripts check structure, app IDs and dates; they cannot verify the reporter's device or observations. The summary counts physical-device and simulator reports separately. Preserve earlier reports when a new version changes behavior so readers can understand the difference.
