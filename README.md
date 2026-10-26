# Awesome iPhone Duo [![Awesome](https://awesome.re/badge.svg)](https://awesome.re) [![Catalog checks](https://github.com/KeWang0622/awesome-iphone-duo/actions/workflows/check.yml/badge.svg)](https://github.com/KeWang0622/awesome-iphone-duo/actions/workflows/check.yml)

**A pocket laptop. A folding game board. An accordion. A notebook that closes.**

A source-linked field guide to interesting things you can do with [Apple's iPhone Duo](https://www.apple.com/iphone-duo/). Find apps by their documented fold interactions, understand what each setup needs, or explore an experiment you can build on.

**169 apps and projects · 142 available · 10 source builds · 11 prototypes · 6 previews**

Latest source review: **2026-10-26**. Individual dates and references live in the [catalog](data/apps.json).

[Browse by interaction](docs/interaction-index.md) · [Pocket laptop guide](docs/laptop-guide.md) · [Things to try](docs/workflows.md) · [Search offline](docs/tooling.md) · [Related projects](docs/landscape.md)

## Start here

| I want to… | Try | What to know |
| --- | --- | --- |
| Turn Duo into a tiny laptop | [Sill](#app-sill), [Headroom](#app-headroom), [Farroom](#app-farroom) | A reachable Mac or PC does the computing. |
| Work on the phone itself | [PXS Desktop](#app-pxs-desktop), [XeOS](#app-xeos) | Web workspaces and built-in tools inside an iPhone app. |
| Run a local emulated PC | [UTM SE](#app-utm-se) | Actual emulation; guest systems are separate and SE has no JIT. |
| Play with a tiny retro computer | [Tiny Computers](#app-tiny-computers) | Interactive recreations with keys, games and paint programs. |
| Make music with the hinge | [Fold Accordion](#app-fold-accordion) | Opening and closing becomes the bellows. |
| Recreate a folding handheld | [Delta](#app-delta-game-emulator) | Pose-aware controls and DS sleep when closed; games are separate. |
| Make something to share | [Papelle](#app-papelle), [Inkblotter](#app-inkblotter) | Folding cards and mirrored ink art. |
| Explore the unusual | [Toastie](#app-toastie-grilled-cheese-game), [Knuckle](#app-knuckle) | Grill a virtual sandwich, or investigate a robot-gripper prototype. |

The [laptop guide](docs/laptop-guide.md) explains the difference between remote desktops, local app workspaces, emulation and retro toys, with setup requirements and limits.

## Reading the list

- **Primary** — Developer documentation, official announcements, release notes or source code explicitly supports the claim.
- **Apple collection** — Apple includes it in a Duo collection; a special hinge feature is not implied.
- **Reported / Community** — Editorial coverage or a public user report; stronger primary evidence is welcome.
- **Build from source / Prototype / Beta / Announced** — Access labels, separate from evidence quality. A prototype may only have a demo.
- **Source** — App source code, subject to its own license and build requirements.

Every interaction tag has a supporting URL. [Hinge input](docs/interaction-index.md#hinge-input), [pose layouts](docs/interaction-index.md#posture-layout), [cover-screen experiences](docs/interaction-index.md#cover-display), [expanded workspaces](docs/interaction-index.md#expanded-layout), and [system multitasking](docs/interaction-index.md#split-view) are distinct; ordinary two-pane layouts do not count as Split View.

This is an AI-assisted, source-researched catalog. **This project has not tested these apps on physical Duo hardware.** [Contribute a reproducible test report](docs/testing.md). Prices, availability and feature versions can change; check the developer's current listing before installing.

## Contents

- [Tiny laptops and remote desktops](#tiny-laptops-and-remote-desktops)
- [Desktop workspaces and terminals](#desktop-workspaces-and-terminals)
- [Notes and writing](#notes-and-writing)
- [Documents and PDFs](#documents-and-pdfs)
- [Planning and focus](#planning-and-focus)
- [Reading and research](#reading-and-research)
- [Photos and video](#photos-and-video)
- [Music and instruments](#music-and-instruments)
- [Games](#games)
- [Playful objects and art](#playful-objects-and-art)
- [Fitness and outdoors](#fitness-and-outdoors)
- [Weather and nature](#weather-and-nature)
- [Travel and navigation](#travel-and-navigation)
- [Communication](#communication)
- [Cooking and everyday](#cooking-and-everyday)
- [Utilities and measurements](#utilities-and-measurements)
- [Source projects and experiments](#source-projects-and-experiments)
- [Previews and watchlist](#previews-and-watchlist)
- [References and related lists](#references-and-related-lists)
- [Contributing](#contributing)

## Tiny laptops and remote desktops

Remote desktops arranged like a miniature laptop. A separate, reachable Mac or PC does the computing; supported hosts and setup vary.

- <a id="app-farroom"></a>[Farroom](https://farroom.danielren.tz/) - Turns the lower half into a trackpad beneath your remote desktop. Supports Mac Screen Sharing, VNC, RDP and Sunshine with a compatible host. [Primary](https://farroom.danielren.tz/).
- <a id="app-headroom"></a>[Headroom](https://apps.apple.com/us/app/headroom-remote-desktop/id6790331904) - Puts your remote Mac above the fold and a keyboard or trackpad below. Uses macOS Screen Sharing; a reachable Mac is required. [Primary](https://apps.apple.com/us/app/headroom-remote-desktop/id6790331904).
- <a id="app-lumendesk"></a>[LumenDesk](https://apps.apple.com/us/app/lumendesk/id6812616599) - Moves a remote Mac workspace between the Duo's laptop layout and USB-C display glasses. Mac streaming requires its companion app and Pro access. [Primary](https://apps.apple.com/us/app/lumendesk/id6812616599) · [Details](https://lumendesk.dev/).
- <a id="app-remio"></a>[Remio](https://github.com/remioapp/releases) - Remote desktop with the computer above the hinge and keyboard below. Requires Remio Host; the linked GitHub repository distributes releases, not app source. [Primary](https://github.com/remioapp/releases).
- <a id="app-scry"></a>[Scry](https://bravely.dev/scry/iphone-duo) - Remote access to Mac, Windows and Linux with layouts for both Duo displays and a partially folded laptop mode. Requires a host computer. [Primary](https://bravely.dev/iphone-duo).
- <a id="app-sill"></a>[Sill](https://github.com/Saffsanity/sill) - Streams a Mac window or desktop with hinge-aware screen, trackpad and keyboard layouts. Open source; requires an Apple silicon Mac and the companion app. [Primary](https://github.com/Saffsanity/sill) · [Source](https://github.com/Saffsanity/sill).

## Desktop workspaces and terminals

Local workspaces, PC emulation and remote terminals. These are different ways to work: check the entry and laptop guide for where computation runs.

- <a id="app-agent-hud"></a>[Agent HUD](https://apps.apple.com/us/app/agent-hud/id6812113619) - Follow AI agents running on your Mac with session details beside the session list and token charts beside recent usage. [Primary](https://apps.apple.com/us/app/agent-hud/id6812113619).
- <a id="app-hey-terminal"></a>[Hey Terminal](https://apps.apple.com/us/app/hey-terminal-ssh-client/id6761189074) - SSH client whose terminal resizes for the inner display, cover screen and Split View. Development tools run on your remote computer. [Primary](https://apps.apple.com/us/app/hey-terminal-ssh-client/id6761189074).
- <a id="app-la-terminal"></a>[La Terminal](https://apps.apple.com/us/app/la-terminal-mosh-ssh-client/id1629902861) - SSH and Mosh terminal with support for open, closed and partially folded Duo use. Remote sessions require a server. [Primary](https://apps.apple.com/us/app/la-terminal-mosh-ssh-client/id1629902861).
- <a id="app-pxs-desktop"></a>[PXS Desktop](https://apps.apple.com/us/app/pxs-external-screen-desktop/id6756102352) - Windowed browser and built-in tools running on the phone, with a desktop above the fold and touchpad below. Also supports external displays. [Primary](https://apps.apple.com/us/app/pxs-external-screen-desktop/id6756102352).
- <a id="app-stealthos"></a>[StealthOS](https://apps.apple.com/us/app/stealthos-private-browser/id6756983634) - An in-app workspace with movable windows, a browser and utilities. Its Duo layout preserves window state while folding and lets windows cross the hinge. [Primary](https://apps.apple.com/us/app/stealthos-private-browser/id6756983634).
- <a id="app-termius"></a>[Termius](https://apps.apple.com/us/app/termius-modern-ssh-client/id549039908) - SSH, Mosh and SFTP client for working on remote machines. Version 8.0.6 adds Duo support; the release notes do not specify a hinge-controlled interface. [Primary](https://apps.apple.com/us/app/termius-modern-ssh-client/id549039908).
- <a id="app-utm-se"></a>[UTM SE](https://apps.apple.com/us/app/utm-se-retro-pc-emulator/id1564628856) - Run a local emulated computer with its screen above the hinge and a keyboard or touchpad below in laptop pose. [Primary](https://github.com/utmapp/UTM/releases/tag/v5.0.8) · [Details](https://docs.getutm.app/installation/ios/) · [Source](https://github.com/utmapp/UTM). **Needs / limits:** Local emulation; SE has no JIT or hypervisor. The documented Duo laptop mode requires iOS 27.1; guest systems are separate.
- <a id="app-xeos"></a>[XeOS](https://desktopmodeiphone.com/) - A windowed web workspace for the Duo and external screens, with files and browser tools. Version 2.8 adds Duo support and a second-screen workflow. [Primary](https://apps.apple.com/id/app/external-display-desktop-xeos/id6758286241).

## Notes and writing

Notebooks, sketches and writing tools adapted to the fold or expanded display.

- <a id="app-agenda"></a>[Agenda](https://apps.apple.com/us/app/agenda-notes-meets-calendar/id1370289240) - Partially fold a date-based notebook so its sidebar and notes sit on opposite sides of the hinge. [Primary](https://apps.apple.com/us/app/agenda-notes-meets-calendar/id1370289240).
- <a id="app-bear"></a>[Bear](https://apps.apple.com/vu/app/bear-markdown-notes/id1016366447) - Markdown notes and linked writing with an explicitly released Duo update, refreshed panels and improved table sizing. [Primary](https://apps.apple.com/vu/app/bear-markdown-notes/id1016366447).
- <a id="app-capture"></a>[Capture](https://apps.apple.com/us/app/quick-notes-capture/id6458535284) - Browse captured ideas beside the selected note, photo or link on the open display. [Primary](https://apps.apple.com/us/app/quick-notes-capture/id6458535284).
- <a id="app-concepts"></a>[Concepts](https://apps.apple.com/us/app/concepts/id560586497) - Sketch on a canvas whose gallery and tool placement adjust as you fold and unfold the device. [Primary](https://apps.apple.com/us/app/concepts/id560586497).
- <a id="app-craft"></a>[Craft](https://apps.apple.com/us/app/craft-notes-documents-ai/id1487937127) - Continue working on documents, tasks and Daily Notes across the inner and cover displays. [Primary](https://apps.apple.com/us/app/craft-notes-documents-ai/id1487937127).
- <a id="app-flow"></a>[Flow](https://apps.apple.com/us/app/flow-note-taking-sketchbook/id1271361459) - Start a sketch on the cover screen and unfold it into a larger notebook that adjusts to how you hold Duo. [Primary](https://apps.apple.com/us/app/flow-note-taking-sketchbook/id1271361459).
- <a id="app-grammarly"></a>[Grammarly](https://apps.apple.com/us/app/grammarly-ai-keyboard-voice/id1158877342) - Type with a split keyboard introduced alongside the app's Duo adaptation. [Primary](https://apps.apple.com/us/app/grammarly-ai-keyboard-voice/id1158877342).
- <a id="app-klavette"></a>[Klavette](https://apps.apple.com/us/app/klavette/id6811542189) - Use a single-row keyboard on the cover screen, then dock or split it along the edges of the unfolded display. [Primary](https://apps.apple.com/us/app/klavette/id6811542189).
- <a id="app-markd-ly"></a>[Markd.ly](https://bravely.dev/markdly/iphone-duo) - Write plain Markdown with the document list beside the editor, keeping text clear of the crease when partly folded. [Primary](https://bravely.dev/markdly/iphone-duo).
- <a id="app-penbook"></a>[Penbook](https://apps.apple.com/us/app/penbook-paper-planner-notes/id1473064295) - Use a two-page digital notebook with stationery sizes and navigation adapted to Duo's poses. [Primary](https://apps.apple.com/us/app/penbook-paper-planner-notes/id1473064295).
- <a id="app-penjo"></a>[Penjo](https://apps.apple.com/us/app/penjo-pencil-journal-planner/id6446053076) - Write on the lower half while calendar events and reminders stand above; folding shut closes the journal. [Primary](https://penjoapp.com/iphone-duo).
- <a id="app-typedraw"></a>[TypeDraw](https://apps.apple.com/us/app/typedraw/id6822194774) - Open the phone like a personal notebook, type in a handwriting font, and use a two-page spread when held sideways. [Primary](https://apps.apple.com/us/app/typedraw/id6822194774). **Needs / limits:** The listing describes Apple Pencil on Duo as coming later; current input includes typing and finger drawing.

## Documents and PDFs

Compare, edit and sign documents with more room for pages and controls.

- <a id="app-asapdf"></a>[ASAPDF](https://bravely.dev/asapdf/iphone-duo) - Edit or sign a PDF with the active page assigned its own half of a partially folded screen. [Primary](https://bravely.dev/asapdf/iphone-duo).
- <a id="app-essayist"></a>[Essayist](https://apps.apple.com/us/app/essayist-academic-writing-app/id1537845384) - Write an academic paper on one half of the folded phone while its inspector occupies the other. [Primary](https://apps.apple.com/us/app/essayist-academic-writing-app/id1537845384).
- <a id="app-pdf-expert"></a>[PDF Expert](https://apps.apple.com/us/app/pdf-expert-editor-reader/id743974925) - Open two PDFs together for comparison, then fold back to a compact signing workflow. [Primary](https://apps.apple.com/us/app/pdf-expert-editor-reader/id743974925).
- <a id="app-pitch-mode"></a>[Pitch Mode](https://apps.apple.com/us/app/pitch-mode-slide-presenter/id6821425392) - Present slides on a TV while Duo holds slide controls beside speaker notes; book pose enlarges the controls. [Primary](https://apps.apple.com/us/app/pitch-mode-slide-presenter/id6821425392).
- <a id="app-scanner-pro"></a>[Scanner Pro](https://apps.apple.com/us/app/scanner-pro-scan-to-pdf/id333710667) - Scan, sign and convert paperwork in a document workflow explicitly updated for the foldable iPhone. [Primary](https://apps.apple.com/us/app/scanner-pro-scan-to-pdf/id333710667).

## Planning and focus

Calendars, tasks and timers that use the extra space or a propped-up pose.

- <a id="app-actions"></a>[Actions](https://apps.apple.com/us/app/actions-to-do-list-organizer/id1227402276) - Keep today's and tomorrow's schedule visible alongside any task list as the phone opens or partially folds. [Primary](https://apps.apple.com/us/app/actions-to-do-list-organizer/id1227402276).
- <a id="app-calendars-by-readdle"></a>[Calendars by Readdle](https://apps.apple.com/us/app/calendars-schedule-planner/id608834326) - Unfold for expanded calendar views, an agenda beside its timeline, and a sidebar for switching schedules. [Primary](https://apps.apple.com/us/app/calendars-schedule-planner/id608834326).
- <a id="app-daylish"></a>[Daylish](https://apps.apple.com/us/app/daylish-visual-schedule/id6751201325) - Prop Duo in tent or laptop pose to show the current or next schedule item as a large desk display. [Primary](https://apps.apple.com/us/app/daylish-visual-schedule/id6751201325).
- <a id="app-eventual"></a>[Eventual](https://apps.apple.com/us/app/eventual-calendar/id6756028875) - A personal calendar with layouts explicitly designed for every Duo pose and orientation. [Primary](https://apps.apple.com/us/app/eventual-calendar/id6756028875).
- <a id="app-fantastical"></a>[Fantastical](https://apps.apple.com/us/app/fantastical-calendar/id718043190) - Create calendar events and tasks in an expanded Duo layout using natural-language input. [Primary](https://apps.apple.com/us/app/fantastical-calendar/id718043190).
- <a id="app-finalist"></a>[Finalist](https://apps.apple.com/us/app/finalist-daily-planner/id6447014685) - Open an agenda beside its timeline, or prop Duo like a small laptop for a clock counting down your schedule. [Primary](https://www.finalist.works/4-2/).
- <a id="app-foldtimer"></a>[FoldTimer](https://apps.apple.com/us/app/foldtimer-focus-pomodoro/id6824176786) - Set a countdown by opening the hinge, then close the phone to start it; unfold for a board of running timers. [Primary](https://apps.apple.com/us/app/foldtimer-focus-pomodoro/id6824176786).
- <a id="app-portal"></a>[Portal](https://apps.apple.com/us/app/portal-escape-into-nature/id1436994560) - Unfold into a nature scene, with focus timers, sleep timers and alarms arranged for closed, flat, seated or standing poses. [Primary](https://apps.apple.com/us/app/portal-escape-into-nature/id1436994560).
- <a id="app-sleepiest"></a>[Sleepiest](https://apps.apple.com/us/app/sleepiest-meditation-for-sleep/id1244690083) - Turn a half-folded Duo into a sleep-sound mixing desk, or use tent pose as a bedside clock with playback controls. [Primary](https://apps.apple.com/us/app/sleepiest-meditation-for-sleep/id1244690083).
- <a id="app-solarday"></a>[Solarday](https://apps.apple.com/us/app/solarday-plan-days-better/id6749725584) - Keep your day's intention beside your task list on the unfolded screen. [Primary](https://apps.apple.com/us/app/solarday-plan-days-better/id6749725584).
- <a id="app-structured"></a>[Structured](https://apps.apple.com/us/app/structured-daily-planner-todo/id1499198946) - Run a visual daily plan with a Focus Timer designed for book and tabletop positions. [Primary](https://apps.apple.com/us/app/structured-daily-planner-todo/id1499198946).
- <a id="app-things-3"></a>[Things 3](https://apps.apple.com/us/app/things-3/id904237743) - Unfold to reveal a list sidebar, use Split View, and connect a keyboard for the full set of task-management shortcuts. [Primary](https://apps.apple.com/us/app/things-3/id904237743).
- <a id="app-tiimo"></a>[Tiimo](https://apps.apple.com/si/app/tiimo-daily-to-do-list/id1480220328) - Prop up a visual focus timer beside routine notes and subtasks. [Primary](https://www.apple.com/newsroom/2026/10/developers-bring-incredible-new-app-experiences-to-iphone-duo/).
- <a id="app-timepage"></a>[Timepage](https://apps.apple.com/us/app/timepage-calendar-planner/id989178902) - Expand a calendar from the cover display into a wider schedule with Duo-specific vertical navigation. [Primary](https://apps.apple.com/us/app/timepage-calendar-planner/id989178902).
- <a id="app-zenitizer"></a>[Zenitizer](https://apps.apple.com/us/app/meditation-timer-zenitizer/id6444767911) - Start a meditation by placing Duo in tent pose, then use a timer laid out around the fold. [Primary](https://apps.apple.com/us/app/meditation-timer-zenitizer/id6444767911).

## Reading and research

Feeds, saved articles and visual thinking. Some entries document layout support without a unique hinge interaction.

- <a id="app-comicflow"></a>[ComicFlow](https://heynavid.com/apps/comicflow/) - Read comics or manga as facing pages, with the gutter aligned to the hinge and your page retained when folding. [Primary](https://heynavid.com/apps/comicflow/).
- <a id="app-faff"></a>[FAFF](https://apps.apple.com/us/app/faff-news-reader-playlists/id6816192280) - Read news on facing pages, close Duo to continue listening, or stand it up as a news radio. [Primary](https://apps.apple.com/us/app/faff-news-reader-playlists/id6816192280).
- <a id="app-goodlinks"></a>[GoodLinks](https://apps.apple.com/ie/app/goodlinks/id1474335294) - Save and annotate reading material in a read-later app whose developer explicitly confirms Duo support. [Primary](https://apps.apple.com/ie/app/goodlinks/id1474335294).
- <a id="app-inoreader"></a>[Inoreader](https://apps.apple.com/us/app/inoreader-news-rss-reader/id892355414) - Unfold into a feed-and-article workspace without losing your reading position; use its compact layout beside another app. [Primary](https://apps.apple.com/us/app/inoreader-news-rss-reader/id892355414).
- <a id="app-instapaper"></a>[Instapaper](https://apps.apple.com/us/app/instapaper/id288545208) - A read-later library with a released Duo update and article narration options. [Primary](https://apps.apple.com/us/app/instapaper/id288545208).
- <a id="app-mandadeck"></a>[MandaDeck](https://apps.apple.com/us/app/hsk-vocab-chinese-mandadeck/id6761324480) - Study Chinese with vocabulary beside its explanation, or stand the closed phone sideways for automatically advancing word cards. [Primary](https://apps.apple.com/us/app/hsk-vocab-chinese-mandadeck/id6761324480).
- <a id="app-xmind"></a>[Xmind](https://apps.apple.com/us/app/xmind-ai-mind-map-brainstorm/id1286983622) - Review an outline alongside its mind map, or open related documents together while developing an idea. [Primary](https://apps.apple.com/us/app/xmind-ai-mind-map-brainstorm/id1286983622).

## Photos and video

Capture, edit, watch and present using the available displays and poses.

- <a id="app-not-boring-camera"></a>[(Not Boring) Camera](https://apps.apple.com/us/app/not-boring-camera/id6737783441) - Frame photos using the cover-display preview, with a camera interface that fills either screen. [Primary](https://apps.apple.com/us/app/not-boring-camera/id6737783441).
- <a id="app-bezel"></a>[Bezel](https://nonstrict.eu/bezel/presskit/2026-10-23-iphone-duo/) - Frame screenshots in Duo poses or animate an unfolding mockup; editing controls move around the hinge on the phone itself. [Primary](https://nonstrict.eu/bezel/presskit/2026-10-23-iphone-duo/).
- <a id="app-blackmagic-camera"></a>[Blackmagic Camera](https://apps.apple.com/us/app/blackmagic-camera/id6449580241) - A professional video camera app with released Duo support; useful when camera control matters more than novelty. [Primary](https://apps.apple.com/us/app/blackmagic-camera/id6449580241).
- <a id="app-clap-film-slate"></a>[Clap: Film Slate](https://apps.apple.com/us/app/clap-film-slate/id6824625416) - Use the phone as a clapperboard: close it to mark a take, then review or annotate that take on the cover. [Primary](https://apps.apple.com/us/app/clap-film-slate/id6824625416). **Needs / limits:** Full use requires Clap Pro after the trial; actual sync accuracy was not independently tested.
- <a id="app-darkroom"></a>[Darkroom](https://apps.apple.com/us/app/darkroom-photo-video-editor/id953286746) - Use the photo editor's iPad-style workflow through an interface responsive to every Duo pose. [Primary](https://apps.apple.com/us/app/darkroom-photo-video-editor/id953286746).
- <a id="app-detail"></a>[Detail](https://apps.apple.com/is/app/detail-ai-video-editor/id1673518618) - Record using the inner, outer or rear camera; send a selfie preview and teleprompter to the cover display, or record both directions in Book Mode. [Primary](https://apps.apple.com/is/app/detail-ai-video-editor/id1673518618).
- <a id="app-dispatch-postcard"></a>[Dispatch Postcard](https://apps.apple.com/us/app/dispatch-postcard/id6794934091) - Build a video postcard with the viewfinder beside its ten-clip deck, or prop Duo up for timed hands-free capture. [Primary](https://apps.apple.com/us/app/dispatch-postcard/id6794934091).
- <a id="app-flashroom"></a>[Flashroom](https://apps.apple.com/us/app/flashroom-retro-photo-booth/id6813983439) - Set up a tabletop photo booth with a guest-facing cover preview and countdown for four-shot photo strips. [Primary](https://apps.apple.com/us/app/flashroom-retro-photo-booth/id6813983439).
- <a id="app-flipcorder-retro-camcorder"></a>[Flipcorder: Retro Camcorder](https://apps.apple.com/us/app/flipcorder-retro-camcorder/id6818168418) - Treat the fold as a camcorder power switch, show subjects a retro preview outside, and close to save a clip. [Primary](https://apps.apple.com/us/app/flipcorder-retro-camcorder/id6818168418). **Needs / limits:** Paid app; clips remain on the phone according to the developer.
- <a id="app-lock-screen-photo-live-widget"></a>[Lock Screen Photo Live Widget](https://apps.apple.com/eg/app/lock-screen-photo-live-widget/id6804017740) - Stand the Duo in a tent to make a photo frame with time and date, or open it for paired photos. [Primary](https://apps.apple.com/eg/app/lock-screen-photo-live-widget/id6804017740). **Needs / limits:** Its separate Lock Screen feature uses Live Activities with an approximately eight-hour system limit.
- <a id="app-lumafusion"></a>[LumaFusion](https://apps.apple.com/us/app/lumafusion/id1062022008) - Edit multitrack video with an interface that adjusts to Duo's different poses and orientations. [Primary](https://apps.apple.com/us/app/lumafusion/id1062022008).
- <a id="app-netflix"></a>[Netflix](https://apps.apple.com/us/app/netflix/id363590051) - Watch in book, tent or tabletop poses with playback controls that reposition and a reflection effect that responds to the hinge. [Primary](https://about.netflix.com/en/news/mobile-experience-that-moves-with-you).
- <a id="app-sixtyfive-camera"></a>[SixtyFive Camera](https://apps.apple.com/us/app/sixtyfive-camera/id6788836035) - Shoot panoramas using a wide finder, a tabletop timed shutter and a mirrored cover-screen preview for your subjects. [Primary](https://apps.apple.com/us/app/sixtyfive-camera/id6788836035).
- <a id="app-snapshots-instant-film-camera"></a>[Snapshots: Instant Film Camera](https://apps.apple.com/kr/app/snapshots-instant-film-camera/id6818673560) - Take a photo with Duo half open, then unfold it to feed the virtual instant print across the display. [Primary](https://cocktail5555.github.io/snapshots/app/).
- <a id="app-teleprompter"></a>[Teleprompter](https://apps.apple.com/us/app/teleprompter/id941620509) - Read a script on the cover display while recording yourself with the rear cameras. [Primary](https://apps.apple.com/us/app/teleprompter/id941620509).

## Music and instruments

Turn the hinge into an instrument or the screen into a miniature music player.

- <a id="app-aura"></a>[Aura](https://github.com/adrbn/aura) - Listen to a Navidrome or Subsonic library with playback on one side of the open Duo and lyrics or the queue beside it. Requires a Navidrome or Subsonic server. [Primary](https://github.com/adrbn/aura#every-device) · [Source](https://github.com/adrbn/aura).
- <a id="app-deck-man-cassette-player"></a>[Deck-Man: Cassette Player](https://apps.apple.com/us/app/deck-man-cassette-player/id6817070335) - Browse music as cassette tapes, insert a tape, and shut the Duo to begin playback. Uses Apple Music or local audio files. [Primary](https://apps.apple.com/us/app/deck-man-cassette-player/id6817070335). **Needs / limits:** Paid; supports Apple Music and local music files. Previously called Duo-Man.
- <a id="app-fold-accordion"></a>[Fold Accordion](https://apps.apple.com/us/app/fold-accordion/id6815058989) - Use the hinge as accordion bellows while playing onscreen keys and learning songs. [Primary](https://apps.apple.com/us/app/fold-accordion/id6815058989). **Needs / limits:** Paid; physical fold mode is Duo-specific, with other input modes on standard iPhones.
- <a id="app-foldissimo-pocket-accordion"></a>[Foldissimo – Pocket Accordion](https://apps.apple.com/us/app/foldissimo-pocket-accordion/id6819312842) - Control accordion airflow by folding speed, add vibrato by shaking, and record a tune. [Primary](https://apps.apple.com/us/app/foldissimo-pocket-accordion/id6819312842). **Needs / limits:** Optional instrument and song purchases; Store description does not itself spell out Duo in its main paragraph.
- <a id="app-foldtune"></a>[FoldTune](https://apps.apple.com/us/app/foldtune/id6824165484) - Pump the hinge as accordion bellows, playing bass and chords on the left and piano notes on the right. [Primary](https://apps.apple.com/us/app/foldtune/id6824165484). **Needs / limits:** Free; synthesized accordion and harmonium voices.
- <a id="app-koala-sampler-beat-maker"></a>[Koala Sampler • Beat Maker](https://apps.apple.com/us/app/koala-sampler-beat-maker/id1449584007) - Sample sounds and build beats with a version explicitly updated for Duo. [Primary](https://apps.apple.com/us/app/koala-sampler-beat-maker/id1449584007). **Needs / limits:** Release notes do not document hinge gestures; avoid claiming MPC-like fold effects.
- <a id="app-md-vinyl-music-app"></a>[MD Vinyl Music App](https://apps.apple.com/us/app/md-vinyl-music-app/id1606306441) - Turn the half-open Duo into a miniature record player with album art above animated vinyl. [Primary](https://apps.apple.com/us/app/md-vinyl-music-app/id1606306441). **Needs / limits:** Music-service requirements and paid options should be checked in the current listing.
- <a id="app-penta-cd-player-changer"></a>[Penta - CD Player & Changer](https://apps.apple.com/us/app/penta-cd-player-changer/id6806427066) - Unfold a virtual CD jewel case, load its disc, then prop the phone up with a CD wallet above the changer tray. [Primary](https://apps.apple.com/us/app/penta-cd-player-changer/id6806427066). **Needs / limits:** Owned albums work without a subscription; Apple Music catalog streaming requires one.
- <a id="app-pianofold-rhythm-game"></a>[PianoFold - Rhythm Game](https://apps.apple.com/us/app/pianofold-rhythm-game/id6822806944) - Put the Duo in laptop pose: camera-backed piano tiles approach pads on the lower screen. [Primary](https://apps.apple.com/us/app/pianofold-rhythm-game/id6822806944). **Needs / limits:** Free beginning chapters; one-time full-game unlock.

## Games

Fold-controlled games, tabletop boards and documented Duo layout adaptations. Specific hinge mechanics are stated only where sourced.

- <a id="app-alibi-daily-mystery-puzzles"></a>[Alibi: Daily Mystery Puzzles](https://apps.apple.com/us/app/alibi-daily-mystery-puzzles/id6790172064) - Open a mystery casebook with a logic board on one page and clues on the other; fold to keep solving outside. [Primary](https://apps.apple.com/us/app/alibi-daily-mystery-puzzles/id6790172064). **Needs / limits:** Additional case archive and hints have paid access.
- <a id="app-battlefleet-duo"></a>[Battlefleet Duo](https://apps.apple.com/us/app/battlefleet-duo/id6811120963) - Set up a folding naval board with your fleet below and enemy waters upright in front. [Primary](https://apps.apple.com/us/app/battlefleet-duo/id6811120963). **Needs / limits:** Two free battles daily; unlimited battles require a one-time purchase.
- <a id="app-blackbox"></a>[Blackbox](https://apps.apple.com/us/app/blackbox/id962969578) - Explore sensor-driven puzzles featured in a roundup of optimized Duo apps. [Reported](https://www.stuff.tv/features/43-iphone-duo-apps-and-games-the-sensible-the-surprising-and-the-gloriously-bonkers/). **Needs / limits:** Duo wording not found in retrieved App Store text; no particular new Duo puzzle verified.
- <a id="app-calcudoku-sudoku-like-puzzle"></a>[Calcudoku · Sudoku-like Puzzle](https://apps.apple.com/us/app/calcudoku-sudoku-like-puzzle/id1195710578) - Play arithmetic grid puzzles with documented Split View and Duo support. [Primary](https://apps.apple.com/us/app/calcudoku-sudoku-like-puzzle/id1195710578). **Needs / limits:** Support claim is brief; no fold-specific gameplay described.
- <a id="app-calm-jigsaw-puzzle-for-adults"></a>[Calm Jigsaw: Puzzle for Adults](https://apps.apple.com/us/app/calm-jigsaw-puzzle-for-adults/id6760758340) - Keep the jigsaw board on one half of the open display and the piece tray on the other. [Primary](https://apps.apple.com/us/app/calm-jigsaw-puzzle-for-adults/id6760758340). **Needs / limits:** Layout adaptation; no hinge-controlled puzzle mechanic is claimed.
- <a id="app-catdoku-cat-logic-puzzles"></a>[Catdoku! Cat Logic Puzzles](https://apps.apple.com/us/app/catdoku-cat-logic-puzzles/id6775778251) - Solve cat-placement logic puzzles in a version explicitly updated for Duo. [Primary](https://apps.apple.com/us/app/catdoku-cat-logic-puzzles/id6775778251). **Needs / limits:** Release notes do not explain a unique fold interaction.
- <a id="app-chonky-corgo-walking-rpg"></a>[Chonky Corgo: Walking RPG](https://apps.apple.com/us/app/chonky-corgo-walking-rpg/id6796920730) - Turn walking into a corgi RPG with a larger Duo view of the adventure. [Primary](https://apps.apple.com/us/app/chonky-corgo-walking-rpg/id6796920730). **Needs / limits:** An earlier developer blog described hinge toys in testing; current Store text confirms wider layouts, not those toys.
- <a id="app-delta-game-emulator"></a>[Delta - Game Emulator](https://apps.apple.com/us/app/delta-game-emulator/id1048524688) - Use pose-aware retro controls and Nintendo DS layouts; close the Duo to put DS games to sleep. [Primary](https://apps.apple.com/us/app/delta-game-emulator/id1048524688). **Needs / limits:** Games are separate from the emulator; regional distribution and optional paid features vary.
- <a id="app-duometry"></a>[Duometry](https://apps.apple.com/us/app/duometry/id6814650592) - Guess target angles by folding the phone; compete with friends or read the hinge angle. [Primary](https://apps.apple.com/us/app/duometry/id6814650592). **Needs / limits:** App Store says compatible hinge devices rather than naming Duo. Secondary corroboration: https://www.macrumors.com/2026/10/23/iphone-duo-fun-apps/
- <a id="app-fleetfold"></a>[FleetFold](https://apps.apple.com/us/app/fleetfold/id6817450309) - Keep targeting on one half and your fleet below, with an optional fold gesture to confirm firing. [Primary](https://apps.apple.com/us/app/fleetfold/id6817450309). **Needs / limits:** First three battles are free; Full Fleet unlocks the game.
- <a id="app-flick-and-field"></a>[Flick and Field](https://apps.apple.com/de/app/flick-and-field/id6824605641) - Stand the phone partly open to turn it into a miniature basketball court, with the hoop and scoreboard above the playing surface. [Primary](https://apps.apple.com/de/app/flick-and-field/id6824605641). **Needs / limits:** Online matches require Game Center; local play works offline.
- <a id="app-fold-party"></a>[Fold Party](https://apps.apple.com/us/app/fold-party/id6820737260) - Pass one phone through party games that use closed, tent, laptop and flat poses. [Primary](https://apps.apple.com/us/app/fold-party/id6820737260). **Needs / limits:** Free games and paid packs; 2–4 players.
- <a id="app-foldfish"></a>[Foldfish](https://apps.apple.com/us/app/foldfish/id6824988199) - Unfold the hinge to prepare a cast, throw the line, and reel fish across a full-width pond. [Primary](https://apps.apple.com/us/app/foldfish/id6824988199). **Needs / limits:** Free with optional purchases; touchscreen alternatives elsewhere.
- <a id="app-foldlings-foldable-friends"></a>[Foldlings: Foldable Friends](https://apps.apple.com/ma/app/foldlings-foldable-friends/id6820174919) - Fold paper pets into existence, tip their habitat toward the crease, and close the phone to bring a companion onto the cover. [Primary](https://apps.apple.com/ma/app/foldlings-foldable-friends/id6820174919). **Needs / limits:** Optional purchases add pets, worlds and cosmetics.
- <a id="app-greens-mini-golf"></a>[Greens: Mini-golf](https://apps.apple.com/us/app/greens-mini-golf/id6815742588) - Putt on the lower half while a caddie camera shows the course above, or unfold for a full course view. [Primary](https://apps.apple.com/us/app/greens-mini-golf/id6815742588). **Needs / limits:** Free courses with a one-time purchase for additional courses.
- <a id="app-hex-armada"></a>[Hex Armada](https://apps.apple.com/us/app/hex-armada/id6761338531) - Play multiplayer naval combat on a hex map with dedicated Duo and landscape layouts. [Primary](https://apps.apple.com/us/app/hex-armada/id6761338531). **Needs / limits:** No detailed hinge behavior documented.
- <a id="app-hexiled"></a>[Hexiled](https://apps.apple.com/us/app/hexiled/id881274996) - Play a hexagonal word game whose laptop layout places a word constellation on the upright half. [Reported](https://www.stuff.tv/features/43-iphone-duo-apps-and-games-the-sensible-the-surprising-and-the-gloriously-bonkers/). **Needs / limits:** Duo/laptop wording not found in retrieved App Store text; retain as editorial evidence.
- <a id="app-hingami-puzzle-origami"></a>[Hingami - Puzzle Origami](https://apps.apple.com/us/app/hingami-puzzle-origami/id6819676482) - Rotate a paper sheet to align its crease with the hinge, then fold the phone to match a target silhouette. [Primary](https://apps.apple.com/us/app/hingami-puzzle-origami/id6819676482). **Needs / limits:** The listing leaves its level count unspecified; do not quote a number.
- <a id="app-marbles-unhinged-folding-maze"></a>[Marbles Unhinged: Folding Maze](https://apps.apple.com/us/app/marbles-unhinged-folding-maze/id6811637729) - Tilt to roll a marble, then bend the hinge to create ramps, walls and drops. [Primary](https://apps.apple.com/us/app/marbles-unhinged-folding-maze/id6811637729). **Needs / limits:** Available app with optional level purchases; the final Unhinged world is marked coming soon, not the whole app.
- <a id="app-nitelore"></a>[Nitelore](https://apps.apple.com/us/app/nitelore/id6790147739) - Play neon anti-gravity racing with an update that explicitly supports Duo. [Primary](https://apps.apple.com/us/app/nitelore/id6790147739). **Needs / limits:** The release notes do not identify a hinge mechanic; classify as an optimized game.
- <a id="app-nonogram-ultra"></a>[Nonogram Ultra](https://apps.apple.com/us/app/nonogram-ultra/id6799545084) - Solve picture-logic grids and daily challenges in a Duo-optimized version. [Primary](https://apps.apple.com/us/app/nonogram-ultra/id6799545084). **Needs / limits:** No specific hinge mechanic documented.
- <a id="app-orisuji"></a>[Orisuji](https://apps.apple.com/us/app/orisuji/id6817092898) - Fold a paper maze to join paths, move characters, and continue the combined puzzle on the cover display. [Primary](https://apps.apple.com/us/app/orisuji/id6817092898). **Needs / limits:** Paid; tap/pinch alternatives on other devices.
- <a id="app-peekaboard-2-player-games"></a>[Peekaboard: 2 Player Games](https://apps.apple.com/us/app/peekaboard-2-player-games/id6819004793) - Share a flat tabletop for naval battles or liar's dice, then fold your half toward you to peek at hidden information. [Primary](https://apps.apple.com/us/app/peekaboard-2-player-games/id6819004793). **Needs / limits:** Naval Duel is included; the one-time Full Pass unlocks Bluff Cups.
- <a id="app-pixelogic-daily-nonograms"></a>[Pixelogic - Daily Nonograms](https://apps.apple.com/us/app/pixelogic-daily-nonograms/id318667196) - Solve daily nonograms with an update explicitly adding Duo support. [Primary](https://apps.apple.com/us/app/pixelogic-daily-nonograms/id318667196). **Needs / limits:** The release note does not explain a hinge-specific feature.
- <a id="app-toastie-grilled-cheese-game"></a>[Toastie: grilled cheese game](https://apps.apple.com/us/app/toastie-grilled-cheese-game/id6813841355) - Build a sandwich, fold the phone to grill it, and reopen before it burns. [Primary](https://apps.apple.com/us/app/toastie-grilled-cheese-game/id6813841355). **Needs / limits:** Paid app.
- <a id="app-torpedo-sea-battle-2-player"></a>[Torpedo: Sea Battle 2 Player](https://apps.apple.com/us/app/torpedo-sea-battle-2-player/id6817928839) - Use the half-open phone as a folding sea-battle case or give each board a page in book pose. [Primary](https://apps.apple.com/us/app/torpedo-sea-battle-2-player/id6817928839). **Needs / limits:** Distinct from Battlefleet Duo; board orientation is opposite. Optional purchases.
- <a id="app-tumble-gravity-block-puzzle"></a>[Tumble: Gravity Block Puzzle](https://apps.apple.com/us/app/tumble-gravity-block-puzzle/id6810856219) - Separate puzzle board and pieces in book pose, or move touch controls below the fold in laptop pose. [Primary](https://apps.apple.com/us/app/tumble-gravity-block-puzzle/id6810856219). **Needs / limits:** Free with ads; a purchase removes ads.
- <a id="app-twofold-pass-play"></a>[Twofold: Pass & Play](https://apps.apple.com/us/app/twofold-pass-play/id6816330259) - Half-fold to hide a player's board, then close the phone to hand over the next turn privately. [Primary](https://apps.apple.com/us/app/twofold-pass-play/id6816330259). **Needs / limits:** Try each game once; one-time per-game or all-game unlocks.

## Playful objects and art

Small surprises that make the physical shape of the phone part of the experience.

- <a id="app-chompduo"></a>[ChompDuo](https://apps.apple.com/us/app/chompduo/id6823172460) - Show eyes on the cover, open a monster mouth inside, and fold to make its jaws bite. [Primary](https://apps.apple.com/us/app/chompduo/id6823172460). **Needs / limits:** One free monster; other monsters have a one-time unlock.
- <a id="app-dexfold"></a>[DexFold](https://apps.apple.com/us/app/dexfold/id6820194843) - A talking fan-made Pokédex with a red outer lid, a keypad inside, and stats that appear when you partly fold it. [Primary](https://apps.apple.com/us/app/dexfold/id6820194843). **Needs / limits:** Unofficial Pokémon fan app; optional Plus purchase unlocks tracking and customization.
- <a id="app-fold-squish-butterfly-paint"></a>[Fold & Squish: Butterfly Paint](https://apps.apple.com/us/app/fold-squish-butterfly-paint/id6822789179) - Make mirrored paint prints: close the Duo, rub its outer screen, then reopen the painting. [Primary](https://apps.apple.com/us/app/fold-squish-butterfly-paint/id6822789179). **Needs / limits:** Free tools; optional one-time Sparkle Pack.
- <a id="app-fold-crack-cracked-screen"></a>[Fold Crack: Cracked Screen](https://apps.apple.com/de/app/fold-crack-cracked-screen/id6807880115) - A prank screen that develops fake cracks and plays sound effects in response to folding. [Primary](https://apps.apple.com/de/app/fold-crack-cracked-screen/id6807880115). **Needs / limits:** Visual and sound simulation only.
- <a id="app-inkblotter"></a>[Inkblotter](https://apps.apple.com/us/app/inkblotter/id6819932681) - Drop ink, close the phone to press it, then reopen a mirrored blot; its closed cover becomes a dark notebook. [Primary](https://apps.apple.com/us/app/inkblotter/id6819932681). **Needs / limits:** The fictional Examiner is entertainment, not a psychological assessment.
- <a id="app-kami-hinge-driven-origami"></a>[kami: hinge driven origami](https://apps.apple.com/us/app/kami-hinge-driven-origami/id6810977836) - Fold virtual paper by moving the phone's hinge, including creases, stacking and reverse folds. [Primary](https://apps.apple.com/us/app/kami-hinge-driven-origami/id6810977836). **Needs / limits:** A creative toy with no listed levels; real-device performance not tested here.
- <a id="app-lake-coloring-book-for-adults"></a>[Lake: Coloring Book for Adults](https://apps.apple.com/us/app/lake-coloring-book-for-adults/id1183717726) - Unfold an adult coloring book into a larger canvas for detailed artwork. [Primary](https://apps.apple.com/us/app/lake-coloring-book-for-adults/id1183717726). **Needs / limits:** Full library has paid access; avoid presenting planned Pencil support as already delivered.
- <a id="app-origami-fold-learn"></a>[Origami - Fold & Learn](https://apps.apple.com/us/app/origami-fold-learn/id1256478184) - Follow one paper-folding step on the closed phone, then open a book-like view of the finished model beside its instructions. [Primary](https://apps.apple.com/us/app/origami-fold-learn/id1256478184). **Needs / limits:** Teaches folding physical paper; full instruction library requires Premium.
- <a id="app-paint-fold"></a>[Paint & Fold](https://apps.apple.com/ru/app/paint-fold/id6817731303) - Paint on either page, fold to press the colors together, and peel it open; closing speed and dwell time change the print. [Primary](https://apps.apple.com/ru/app/paint-fold/id6817731303). **Needs / limits:** Requires iOS 27 or later.
- <a id="app-panic-tracker-the-red-button"></a>[Panic Tracker: The Red Button](https://apps.apple.com/lk/app/panic-tracker-the-red-button/id6743371838) - A playful red-button counter that also counts closing the Duo as a press. [Primary](https://apps.apple.com/lk/app/panic-tracker-the-red-button/id6743371838). **Needs / limits:** A novelty counter; no health-effect claim is made here.
- <a id="app-papelle"></a>[Papelle](https://apps.apple.com/us/app/papelle/id6816144743) - Interactive greeting cards reveal photos, messages and video as you open the phone; pause the fold to hold the surprise. [Primary](https://apps.apple.com/us/app/papelle/id6816144743). **Needs / limits:** Recipients need the free Papelle app; optional design collections are paid.
- <a id="app-tiny-computers"></a>[Tiny Computers](https://apps.apple.com/app/id6816896250) - Explore ten interactive retro computers with a screen above the fold and keyboard below, including drawing programs and games. A playful recreation rather than a general-purpose operating system. [Primary](https://www.fountaininteractive.com/TinyComputers/press/).
- <a id="app-unfold-your-city"></a>[Unfold Your City](https://apps.apple.com/us/app/unfold-your-city/id6821145773) - Unfold miniature paper cities from an atlas cover; flatten the book to bring on dusk, illuminated windows and music. [Primary](https://apps.apple.com/us/app/unfold-your-city/id6821145773). **Needs / limits:** Barcelona is free; other cities or the full collection are paid.

## Fitness and outdoors

Workout dashboards and outdoor tools with documented Duo layouts.

- <a id="app-gymverse"></a>[Gymverse](https://apps.apple.com/us/app/gymverse-gym-workout-planner/id1048454034) - Show a gym status sign on the cover display, or open Duo to keep your training plan beside today's workout. [Primary](https://gymverse.app/iphone-duo/).
- <a id="app-liftin"></a>[Liftin'](https://liftinapp.co/) - Use the partially folded phone to keep a workout routine and the selected exercise's sets visible across the hinge. [Primary](https://liftinapp.co/).
- <a id="app-personal-best"></a>[Personal Best](https://apps.apple.com/us/app/workout-stats-personal-best/id1510256676) - Replay workouts in a laptop-style seated layout, or inspect activity summaries alongside the workout list. [Primary](https://getpersonalbest.com/duo).
- <a id="app-score-keeper"></a>[Score Keeper](https://apps.apple.com/us/app/score-keeper/id6759308591) - Show large scores on the upright half while keeping scoring buttons and a timer on the flat half. [Primary](https://apps.apple.com/us/app/score-keeper/id6759308591).
- <a id="app-slopes"></a>[Slopes](https://apps.apple.com/it/app/slopes-sci-e-snowboard/id643351983) - Start with a compact ski-tracking interface, then unfold for a much larger trail map. [Primary](https://apps.apple.com/it/app/slopes-sci-e-snowboard/id643351983).
- <a id="app-smartgym"></a>[SmartGym](https://apps.apple.com/us/app/smartgym-gym-home-workouts/id922744883) - Keep routines beside exercise details in book pose, or prop up a workout with live heart-rate and calorie controls below. [Primary](https://apps.apple.com/us/app/smartgym-gym-home-workouts/id922744883).
- <a id="app-wakeout"></a>[Wakeout](https://apps.apple.com/us/app/wakeout-fitness-games/id1242116567) - Prop Duo in tent or laptop pose for hands-free workouts; movement games use the half with the camera. [Primary](https://apps.apple.com/us/app/wakeout-fitness-games/id1242116567).

## Weather and nature

Use the expanded display for forecasts, maps and comparisons.

- <a id="app-carrot-weather"></a>[CARROT Weather](https://apps.apple.com/us/app/carrot-weather-alerts-radar/id961390574) - Compare weather information using dual-pane radar or multiple windows on the expanded display. [Primary](https://apps.apple.com/us/app/carrot-weather-alerts-radar/id961390574).
- <a id="app-mercury-weather"></a>[Mercury Weather](https://apps.apple.com/us/app/mercury-weather/id1621800675) - Unfold to keep saved places beside their forecast, or compare two locations in separate Mercury windows. [Primary](https://apps.apple.com/us/app/mercury-weather/id1621800675).
- <a id="app-please-don-t-rain"></a>[Please Don't Rain](https://apps.apple.com/us/app/please-dont-rain/id6444577668) - Compare weather panels in book pose, or prop Duo like a laptop to jump between forecast charts. [Primary](https://apps.apple.com/us/app/please-dont-rain/id6444577668).
- <a id="app-tide-guide"></a>[Tide Guide](https://apps.apple.com/us/app/tide-guide-charts-tables/id1406371071) - Expand tide charts and lunar details, or inspect weather radar together with tide stations. [Primary](https://apps.apple.com/us/app/tide-guide-charts-tables/id1406371071).

## Travel and navigation

Plan a journey or follow it with layouts that adapt to the phone.

- <a id="app-bikemap"></a>[Bikemap](https://apps.apple.com/us/app/bikemap-bicycle-tracker-gps/id625759466) - Unfold for a larger cycling-route map, with layouts that adapt when folded or rotated. [Primary](https://apps.apple.com/us/app/bikemap-bicycle-tracker-gps/id625759466).
- <a id="app-chimani"></a>[Chimani](https://apps.apple.com/us/app/chimani-national-parks/id436381327) - Explore a park itinerary or guide alongside its interactive map on the unfolded screen. [Primary](https://apps.apple.com/us/app/chimani-national-parks/id436381327).
- <a id="app-flighty"></a>[Flighty](https://apps.apple.com/us/app/flighty-live-flight-tracker/id1358823008) - Turn a tray table into a flight-information display by propping Duo in a tent for hands-free journey tracking. [Primary](https://apps.apple.com/us/app/flighty-live-flight-tracker/id1358823008).
- <a id="app-tripsy"></a>[Tripsy](https://apps.apple.com/us/app/tripsy-travel-planner/id1429967544) - Organize itineraries, trip notes and activity details with navigation and toolbars adapted to Duo. [Primary](https://apps.apple.com/us/app/tripsy-travel-planner/id1429967544).
- <a id="app-true-skies"></a>[True Skies](https://apps.apple.com/us/app/true-skies-flight-tracker/id6751201769) - Track flights beside the live map, with a flight log that opens like a passport when Duo unfolds. [Primary](https://apps.apple.com/us/app/true-skies-flight-tracker/id6751201769).

## Communication

Messages and collaboration with documented Duo support.

- <a id="app-airmail"></a>[Airmail](https://apps.apple.com/us/app/airmail-for-gmail-outlook-mail/id993160329) - Keep the inbox visible while reading messages. [Primary](https://www.apple.com/newsroom/2026/10/developers-bring-incredible-new-app-experiences-to-iphone-duo/).

## Cooking and everyday

Everyday workflows made more useful by the folding display.

- <a id="app-flicit"></a>[Flicit](https://apps.apple.com/us/app/flicit-movie-diary-tickets/id6790159773) - Keep a film diary as tickets; in laptop pose, the ticket stands above the cinema seat diagram. [Primary](https://apps.apple.com/us/app/flicit-movie-diary-tickets/id6790159773).
- <a id="app-menu-planner-2"></a>[Menu Planner 2](https://www.menu-planner.com/iphone-duo) - Prop a recipe upright above its ingredients and timers, or open flat for a week of meals. [Primary](https://www.menu-planner.com/iphone-duo).
- <a id="app-roomantic"></a>[Roomantic](https://apps.apple.com/us/app/roomantic-furniture-planner/id6759999318) - Plan room furnishings across a workspace arranged as two pages at the fold. [Primary](https://apps.apple.com/us/app/roomantic-furniture-planner/id6759999318).
- <a id="app-spread-recipe-book"></a>[Spread: Recipe Book](https://apps.apple.com/us/app/spread-recipe-book/id6820745043) - Cook from ingredients on one page and the current instruction on the other, with the hinge between them. [Primary](https://apps.apple.com/us/app/spread-recipe-book/id6820745043).

## Utilities and measurements

Hinge measurements and small tools with a documented Duo-specific use.

- <a id="app-foldlab"></a>[FoldLab](https://apps.apple.com/us/app/foldlab-hinge-fold-tools/id6814885312) - Read hinge angles, save reference targets and use slope or miter tools, with a companion reading on the cover. [Primary](https://apps.apple.com/us/app/foldlab-hinge-fold-tools/id6814885312).
- <a id="app-hinge-caliper"></a>[Hinge Caliper](https://apps.apple.com/us/app/hinge-caliper/id6819039427) - Estimate an object's thickness from the hinge angle, with an optional spoken reading and cover-display measurement. [Primary](https://apps.apple.com/us/app/hinge-caliper/id6819039427).
- <a id="app-outspan"></a>[OutSpan](https://apps.apple.com/us/app/outspan/id6814314176) - Expand Safari pages underneath its side controls on Duo's cover display or while browsing beside another app. [Primary](https://apps.apple.com/us/app/outspan/id6814314176).

## Source projects and experiments

Source projects and research prototypes, separate from ordinary downloads. A prototype may have no public build; code availability does not establish an open-source license or successful hardware testing.

- <a id="app-accorduon"></a>[Accorduon](https://github.com/artemnovichkov/Accorduon) - Play a virtual accordion whose volume and tone respond to hinge movement, with melody keys on one side and bass buttons on the other. [Primary](https://github.com/artemnovichkov/Accorduon#readme) · Build from source · [Source](https://github.com/artemnovichkov/Accorduon).
- <a id="app-askmeety"></a>[AskMeety](https://devpost.com/software/halfnote) - A meeting-note prototype that folds into video above a scratchpad, collecting approved transcript excerpts and captured frames. [Primary](https://devpost.com/software/halfnote) · Prototype. **Needs / limits:** Real-meeting audio capture, physical hinge behavior and end-to-end exports still need hardware validation.
- <a id="app-basis"></a>[Basis](https://devpost.com/software/basis-5eykt9) - A hands-on linear algebra demo where folding the phone changes a coordinate basis and reveals what happens near singularity. [Primary](https://devpost.com/software/basis-5eykt9) · Prototype. **Needs / limits:** Simulator prototype. Its claimed simultaneous inner/outer math display is not verified on hardware and is not tagged as a supported cover feature.
- <a id="app-clawkit"></a>[ClawKit](https://github.com/artemnovichkov/ClawKit) - Turn a half-folded Duo into a miniature claw arcade, with the cabinet above the hinge and joystick controls below. [Primary](https://github.com/artemnovichkov/ClawKit#readme) · Build from source · [Source](https://github.com/artemnovichkov/ClawKit).
- <a id="app-crate-iphone-duo-mpc"></a>[Crate — iPhone Duo MPC](https://devpost.com/software/crate-iphone-duo-mpc) - Build beats with pads below, performance information above, and hinge-controlled effects. Hackathon prototype; its creators list physical-device testing as future work. [Primary](https://devpost.com/software/crate-iphone-duo-mpc) · Prototype. **Needs / limits:** Prototype; submission says testing on a physical Duo is future work. Distinct from Crate Music Library.
- <a id="app-duobird"></a>[DuoBird](https://github.com/artemnovichkov/DuoBird) - Steer a bird through gaps by opening the hinge to flap, with touch controls as a fallback. [Primary](https://github.com/artemnovichkov/DuoBird#readme) · Build from source · [Source](https://github.com/artemnovichkov/DuoBird).
- <a id="app-duocut"></a>[DuoCut](https://github.com/artemnovichkov/DuoCut) - Move shapes across the crease and fold to slice them in daily, puzzle, and arcade challenges. [Primary](https://github.com/artemnovichkov/DuoCut#readme) · Build from source · [Source](https://github.com/artemnovichkov/DuoCut).
- <a id="app-duogami"></a>[Duogami](https://github.com/artemnovichkov/Duogami) - Fold the device to crease virtual origami, follow guided animal lessons, or experiment with a blank sheet. [Primary](https://github.com/artemnovichkov/Duogami#readme) · Build from source · [Source](https://github.com/artemnovichkov/Duogami).
- <a id="app-duoremote"></a>[DuoRemote](https://github.com/yezzer/DuoRemote) - Mac Screen Sharing client with a laptop pose, trackpad and modifier keys below the fold. Build with Xcode; requires iOS 27.1 and a reachable Mac. [Primary](https://github.com/yezzer/DuoRemote) · Build from source · [Source](https://github.com/yezzer/DuoRemote).
- <a id="app-factorio-native-port"></a>[Factorio native port](https://github.com/d4m14ndx/factorio-native-arm-ipad) - Run an experimental native Factorio port on Duo with touch, an on-screen keyboard, and Bluetooth keyboard or trackpad controls. Requires a purchased game, compatible Mac and local signing; fold transitions remain untested by its maintainer. [Primary](https://github.com/d4m14ndx/factorio-native-arm-ipad#readme) · Build from source · [Source](https://github.com/d4m14ndx/factorio-native-arm-ipad).
- <a id="app-foldrush"></a>[FoldRush](https://github.com/AskArtwentythree/foldrush) - Bend the hinge to jump and tilt to steer through a 3D running course. Public source; no root license was found. [Primary](https://github.com/AskArtwentythree/foldrush#readme) · Build from source · [Source](https://github.com/AskArtwentythree/foldrush).
- <a id="app-foldtales-pop-up-storybook"></a>[Foldtales: pop-up storybook](https://devpost.com/software/foldtales-the-pop-up-book-that-stands-up-inside-the-fold) - A paper storybook prototype with hinge-raised scenery, an outer cover and a laptop pose that becomes a narrated bedtime stage. [Primary](https://devpost.com/software/foldtales-the-pop-up-book-that-stands-up-inside-the-fold) · Prototype. **Needs / limits:** Simulator prototype; its linked GitHub repository returned 404. Distinct from the unrelated FoldTales wallpaper app.
- <a id="app-knuckle"></a>[Knuckle](https://devpost.com/software/knuckle) - Use the hinge to open and close a robot gripper, record a demonstration, replay it, and export the motion data. [Primary](https://devpost.com/software/knuckle) · Prototype · [Source](https://github.com/keming-jiao/knuckle). **Needs / limits:** Hackathon prototype requiring robot hardware and a bridge. Replays demonstrations; it does not train a model.
- <a id="app-monster-ink"></a>[Monster, Ink.](https://devpost.com/software/monster-ink) - A focus-game prototype where a cat builds a city on the closed cover; opening the phone releases a destructive monster. [Primary](https://devpost.com/software/monster-ink) · Prototype · [Source](https://github.com/PujaSridhar/Monsters-Ink.). **Needs / limits:** Hackathon source prototype; hardware haptics and actual Screen Time/Focus integration remain future work.
- <a id="app-pop"></a>[Pop!](https://devpost.com/software/pop-03ba9g) - Create a spoken picture book, fold to turn its pages, and angle the phone to reveal pop-up scenes or add the next story instruction. [Primary](https://devpost.com/software/pop-03ba9g) · Prototype. **Needs / limits:** Simulator prototype with cloud generation services; linked GitHub repository returned 404.
- <a id="app-pop-up-post"></a>[Pop-Up Post](https://devpost.com/software/pop-up-post) - Run through a pop-up book, folding to flatten obstacles and opening to raise bridges; closing pauses on the book cover. [Primary](https://devpost.com/software/pop-up-post) · Prototype · [Source](https://github.com/FelixIsaac/pop-up-post). **Needs / limits:** Source prototype built for the Duo simulator; not a verified App Store release.
- <a id="app-pulse-the-pocket-dj-deck"></a>[Pulse - the pocket DJ deck](https://devpost.com/software/pulse-the-pocket-dj-deck) - A pocket DJ prototype with waveforms above performance controls and hinge-driven pitch, filters, time stretch or scrubbing. [Primary](https://devpost.com/software/pulse-the-pocket-dj-deck) · Prototype · [Source](https://github.com/rishi-thak/pulse). **Needs / limits:** Hackathon source prototype; hardware tuning and performance recording/export remain planned.
- <a id="app-sand-valley"></a>[Sand Valley](https://github.com/artemnovichkov/SandValley) - Pour virtual sand and fold the phone to send the grains toward the crease. [Primary](https://github.com/artemnovichkov/SandValley#readme) · Build from source · [Source](https://github.com/artemnovichkov/SandValley).
- <a id="app-secchain"></a>[SecChain](https://github.com/bannzai/SecChain) - Manage repository secrets and approve paired Mac requests from an iOS companion with layouts captured on Duo's cover and inner displays. [Primary](https://github.com/bannzai/SecChain/pull/88) · Build from source · [Source](https://github.com/bannzai/SecChain).
- <a id="app-slam"></a>[SLAM](https://devpost.com/software/slam-awqbse) - Place a song on each panel, fold to blend them, then move to the cover to hear the generated mashup. [Primary](https://devpost.com/software/slam-awqbse) · Prototype. **Needs / limits:** Simulator prototype with backend services; arbitrary streaming-library integration is future work.
- <a id="app-unhinged"></a>[Unhinged](https://devpost.com/software/unhinged-mec7yp) - A simulator prototype that turns hinge movement into tilt commands for a real motorized camera rig. [Primary](https://devpost.com/software/unhinged-mec7yp) · Prototype · [Source](https://github.com/SamisLife/unhinged). **Needs / limits:** Requires external camera rig, microcontroller and desktop bridge; simulator demo, not an App Store release.

## Previews and watchlist

Promising ideas whose availability is beta, announced or unconfirmed. A demo or developer claim is not a released feature.

- <a id="app-crate-music-library"></a>[Crate Music Library](https://cratemusicapp.com/) - Browse records and liner notes on facing pages, or place playback above the hinge and notes below. [Primary](https://cratemusicapp.com/) · Beta. **Needs / limits:** TestFlight beta; coming soon to App Store. Distinct from the Crate MPC hackathon project.
- <a id="app-fold-clock"></a>[Fold Clock](https://bravely.dev/foldclock) - A planned bedside clock that separates the time from ambient-sound controls when Duo is partially folded. [Primary](https://bravely.dev/foldclock) · Announced.
- <a id="app-foldremote"></a>[FoldRemote](https://foldremote.app/) - Announced Mac remote client for the Duo opened flat in landscape. Its site says App Store approval is pending and explicitly excludes folded use. [Primary](https://foldremote.app/) · Announced.
- <a id="app-keep-it-shut"></a>[Keep It Shut](https://tenthroomstudio.com/keepitshut/) - An announced horror game where the phone is a hotel-room door: close it for safety, crack it to peek, and open it to expose the hallway. [Primary](https://tenthroomstudio.com/keepitshut/) · Announced. **Needs / limits:** Official release date remains unannounced; no App Store download was verified.
- <a id="app-picloom"></a>[PicLoom](https://apps.apple.com/us/app/picloom-photo-sort-journal/id6812507597) - Preview of a photo journal whose cover opens with the hinge, with a desk-calendar layout when partly folded. [Primary](https://www.reddit.com/r/iosapps/comments/1xahwvh/i_made_journals_open_like_real_books_on_the/) · Announced.
- <a id="app-takealong"></a>[Takealong](https://takealong.app/index.html) - Preview of Mac remote access with a seated keyboard or trackpad layout. The inspected install button leads to TestFlight despite App Store wording. [Primary](https://takealong.app/index.html) · Beta.

## References and related lists

### Apple

- [iPhone Duo](https://www.apple.com/iphone-duo/) - Official device overview.
- [Great Apps and Games on iPhone Duo](https://apps.apple.com/us/iphone/story/id6820639500) - Apple's launch collection.
- [Developer app showcase](https://www.apple.com/newsroom/2026/10/developers-bring-incredible-new-app-experiences-to-iphone-duo/) - Apple's October 22 overview; some updates are described as forthcoming.
- [Prepare and submit your apps for iPhone Duo](https://developer.apple.com/news/?id=kkphp5qo) - Official developer starting point.

### Discovery and further reading

- [MacRumors: tiny computers, a toaster and a DS](https://www.macrumors.com/2026/10/23/iphone-duo-fun-apps/) - Creative app discovery.
- [Stuff: 43 iPhone Duo apps and games](https://www.stuff.tv/features/43-iphone-duo-apps-and-games-the-sensible-the-surprising-and-the-gloriously-bonkers/) - A broad launch roundup.
- [T3: apps for day one](https://www.t3.com/tech/iphones/the-best-iphone-duo-apps-to-download-on-day-one) - Includes both releases and previews.
- [Tom's Guide: 15 app picks](https://www.tomsguide.com/phones/iphones/ive-been-testing-dozens-of-iphone-duo-apps-heres-my-top-15-picks-so-far) - Reviewer impressions; this project's own entries remain untested.

For a comparison of ten app directories and repositories, see the [landscape review](docs/landscape.md). These projects overlap with this catalog and are useful places to discover further leads.

### Related repositories

- [Awesome](https://github.com/sindresorhus/awesome) - The original awesome-list ecosystem and conventions.
- [Awesome Mac](https://github.com/jaywcjlove/awesome-mac) - A useful model for organizing end-user software.
- [Awesome iOS](https://github.com/vsouza/awesome-ios) - Libraries and resources for iOS developers.
- [Open-Source iOS Apps](https://github.com/dkhamsing/open-source-ios-apps) - A complementary source-code catalog, including Duo projects.
- [mergisi/awesome-iphone-duo](https://github.com/mergisi/awesome-iphone-duo) - A developer-focused Duo list and sample.
- [Duo development resources](docs/developer-resources.md) - Examples, hinge tools and community simulators.

## Contributing

Found an ingenious app or an inaccurate claim? [Suggest it or send a correction](https://github.com/KeWang0622/awesome-iphone-duo/issues/new/choose). Read the [contribution guide](CONTRIBUTING.md) for evidence requirements and editing and verification commands.

Original repository content is available under [CC0 1.0](LICENSE). Linked apps and third-party materials retain their own licenses. This is an independent list; the Awesome badge does not imply inclusion in the central directory or endorsement by Apple.
