# Awesome iPhone Duo [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

**A pocket laptop. A folding game board. An accordion. A notebook that closes.**

Interesting apps and experiments for [Apple's iPhone Duo](https://www.apple.com/iphone-duo/), selected for what they do with its fold, inner display, cover screen and different poses.

**110 apps and projects · Sources checked October 26, 2026 · [How this list is researched](docs/research.md)**

## Start here

| I want to… | Try | What to know |
| --- | --- | --- |
| Turn Duo into a tiny laptop | [Sill](https://github.com/Saffsanity/sill), [Headroom](https://apps.apple.com/us/app/headroom-remote-desktop/id6790331904), [Farroom](https://farroom.danielren.tz/) | Remote access; a reachable Mac or PC does the computing. |
| Work on the phone itself | [PXS Desktop](https://apps.apple.com/us/app/pxs-external-screen-desktop/id6756102352), [XeOS](https://desktopmodeiphone.com/) | Windowed web workspaces and built-in tools inside an iPhone app. |
| Play with a tiny retro computer | [Tiny Computers](https://www.fountaininteractive.com/TinyComputers/press/) | Interactive recreations with keys, games and paint programs. |
| Make music with the hinge | [Fold Accordion](https://apps.apple.com/us/app/fold-accordion/id6815058989) | Opening and closing becomes the bellows. |
| Recreate a folding handheld | [Delta](https://apps.apple.com/us/app/delta-game-emulator/id1048524688) | Pose-aware controls and DS sleep when closed; games are separate. |
| Try something wonderfully silly | [Toastie](https://apps.apple.com/us/app/toastie-grilled-cheese-game/id6813841355) | Close the phone to grill a virtual sandwich. |

The desktop-style apps above operate within iOS; they do not install macOS or turn arbitrary native iPhone apps into desktop windows. Remote-desktop apps instead control a separate computer. Details and evidence are linked with each entry below.

## Reading the list

- **Primary** — Developer documentation, official platform announcements, release notes or source code explicitly supports the Duo claim.
- **Apple collection** — Apple includes it in a Duo collection; a special hinge feature is not implied.
- **Reported** — Independent coverage supports the claim; primary Duo documentation was not found.
- **Community** — A user report or demo needs stronger confirmation.
- **Build from source / Beta / Announced** — Availability labels, separate from the evidence rating.
- **Source** — A link to app source, with its own license and build requirements.

This is an AI-assisted, source-researched discovery list. Entries have **not been tested on a physical Duo by this project**. Prices, regional availability and feature versions can change; check the linked listing before installing. The [data file](data/apps.json) records evidence notes and per-entry check dates.

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
- [Source projects and experiments](#source-projects-and-experiments)
- [Previews and watchlist](#previews-and-watchlist)
- [References and related lists](#references-and-related-lists)
- [Contributing](#contributing)

## Tiny laptops and remote desktops

Screen above, keyboard or trackpad below. These apps require a separate, reachable computer; setup and supported host systems vary.

- [Farroom](https://farroom.danielren.tz/) - Turns the lower half into a trackpad beneath your remote desktop. Supports Mac Screen Sharing, VNC, RDP and Sunshine with a compatible host. [Primary](https://farroom.danielren.tz/).
- [Headroom](https://apps.apple.com/us/app/headroom-remote-desktop/id6790331904) - Puts your remote Mac above the fold and a keyboard or trackpad below. Uses macOS Screen Sharing; a reachable Mac is required. [Primary](https://apps.apple.com/us/app/headroom-remote-desktop/id6790331904).
- [LumenDesk](https://apps.apple.com/us/app/lumendesk/id6812616599) - Moves a remote Mac workspace between the Duo's laptop layout and USB-C display glasses. Mac streaming requires its companion app and Pro access. [Primary](https://apps.apple.com/us/app/lumendesk/id6812616599) · [Details](https://lumendesk.dev/).
- [Remio](https://github.com/remioapp/releases) - Remote desktop with the computer above the hinge and keyboard below. Requires Remio Host; the linked GitHub repository distributes releases, not app source. [Primary](https://github.com/remioapp/releases).
- [Scry](https://bravely.dev/scry/iphone-duo) - Remote access to Mac, Windows and Linux with layouts for both Duo displays and a partially folded laptop mode. Requires a host computer. [Primary](https://bravely.dev/iphone-duo).
- [Sill](https://github.com/Saffsanity/sill) - Streams a Mac window or desktop with hinge-aware screen, trackpad and keyboard layouts. Open source; requires an Apple silicon Mac and the companion app. [Primary](https://github.com/Saffsanity/sill) · [Source](https://github.com/Saffsanity/sill).

## Desktop workspaces and terminals

PXS, XeOS and StealthOS provide workspaces within an iPhone app. SSH clients connect to remote machines; read each entry for where the work runs.

- [Hey Terminal](https://apps.apple.com/us/app/hey-terminal-ssh-client/id6761189074) - SSH client whose terminal resizes for the inner display, cover screen and Split View. Development tools run on your remote computer. [Primary](https://apps.apple.com/us/app/hey-terminal-ssh-client/id6761189074).
- [La Terminal](https://apps.apple.com/us/app/la-terminal-mosh-ssh-client/id1629902861) - SSH and Mosh terminal with support for open, closed and partially folded Duo use. Remote sessions require a server. [Primary](https://apps.apple.com/us/app/la-terminal-mosh-ssh-client/id1629902861).
- [PXS Desktop](https://apps.apple.com/us/app/pxs-external-screen-desktop/id6756102352) - Windowed browser and built-in tools running on the phone, with a desktop above the fold and touchpad below. Also supports external displays. [Primary](https://apps.apple.com/us/app/pxs-external-screen-desktop/id6756102352).
- [StealthOS](https://apps.apple.com/us/app/stealthos-private-browser/id6756983634) - An in-app workspace with movable windows, a browser and utilities. Its Duo layout preserves window state while folding and lets windows cross the hinge. [Primary](https://apps.apple.com/us/app/stealthos-private-browser/id6756983634).
- [Termius](https://apps.apple.com/us/app/termius-modern-ssh-client/id549039908) - SSH, Mosh and SFTP client for working on remote machines. Version 8.0.6 adds Duo support; the release notes do not specify a hinge-controlled interface. [Primary](https://apps.apple.com/us/app/termius-modern-ssh-client/id549039908).
- [XeOS](https://desktopmodeiphone.com/) - A windowed web workspace for the Duo and external screens, with files and browser tools. Version 2.8 adds Duo support and a second-screen workflow. [Primary](https://apps.apple.com/id/app/external-display-desktop-xeos/id6758286241).

## Notes and writing

Notebooks, sketches and writing tools adapted to the fold or expanded display.

- [Agenda](https://apps.apple.com/us/app/agenda-notes-meets-calendar/id1370289240) - Partially fold a date-based notebook so its sidebar and notes sit on opposite sides of the hinge. [Primary](https://apps.apple.com/us/app/agenda-notes-meets-calendar/id1370289240).
- [Bear](https://apps.apple.com/vu/app/bear-markdown-notes/id1016366447) - Markdown notes and linked writing with an explicitly released Duo update, refreshed panels and improved table sizing. [Primary](https://apps.apple.com/vu/app/bear-markdown-notes/id1016366447).
- [Concepts](https://apps.apple.com/us/app/concepts/id560586497) - Sketch on a canvas whose gallery and tool placement adjust as you fold and unfold the device. [Primary](https://apps.apple.com/us/app/concepts/id560586497).
- [Craft](https://apps.apple.com/us/app/craft-notes-documents-ai/id1487937127) - Continue working on documents, tasks and Daily Notes across the inner and cover displays. [Primary](https://apps.apple.com/us/app/craft-notes-documents-ai/id1487937127).
- [Flow](https://apps.apple.com/us/app/flow-note-taking-sketchbook/id1271361459) - Start a sketch on the cover screen and unfold it into a larger notebook that adjusts to how you hold Duo. [Primary](https://apps.apple.com/us/app/flow-note-taking-sketchbook/id1271361459).
- [Grammarly](https://apps.apple.com/us/app/grammarly-ai-keyboard-voice/id1158877342) - Type with a split keyboard introduced alongside the app's Duo adaptation. [Primary](https://apps.apple.com/us/app/grammarly-ai-keyboard-voice/id1158877342).
- [Markd.ly](https://bravely.dev/markdly/iphone-duo) - Write plain Markdown with the document list beside the editor, keeping text clear of the crease when partly folded. [Primary](https://bravely.dev/markdly/iphone-duo).
- [Penbook](https://apps.apple.com/us/app/penbook-paper-planner-notes/id1473064295) - Use a two-page digital notebook with stationery sizes and navigation adapted to Duo's poses. [Primary](https://apps.apple.com/us/app/penbook-paper-planner-notes/id1473064295).

## Documents and PDFs

Compare, edit and sign documents with more room for pages and controls.

- [ASAPDF](https://bravely.dev/asapdf/iphone-duo) - Edit or sign a PDF with the active page assigned its own half of a partially folded screen. [Primary](https://bravely.dev/asapdf/iphone-duo).
- [Essayist](https://apps.apple.com/us/app/essayist-academic-writing-app/id1537845384) - Write an academic paper on one half of the folded phone while its inspector occupies the other. [Primary](https://apps.apple.com/us/app/essayist-academic-writing-app/id1537845384).
- [PDF Expert](https://apps.apple.com/us/app/pdf-expert-editor-reader/id743974925) - Open two PDFs together for comparison, then fold back to a compact signing workflow. [Primary](https://apps.apple.com/us/app/pdf-expert-editor-reader/id743974925).
- [Scanner Pro](https://apps.apple.com/us/app/scanner-pro-scan-to-pdf/id333710667) - Scan, sign and convert paperwork in a document workflow explicitly updated for the foldable iPhone. [Primary](https://apps.apple.com/us/app/scanner-pro-scan-to-pdf/id333710667).

## Planning and focus

Calendars, tasks and timers that use the extra space or a propped-up pose.

- [Actions](https://apps.apple.com/us/app/actions-to-do-list-organizer/id1227402276) - Keep today's and tomorrow's schedule visible alongside any task list as the phone opens or partially folds. [Primary](https://apps.apple.com/us/app/actions-to-do-list-organizer/id1227402276).
- [Calendars by Readdle](https://apps.apple.com/us/app/calendars-schedule-planner/id608834326) - Unfold for expanded calendar views, an agenda beside its timeline, and a sidebar for switching schedules. [Primary](https://apps.apple.com/us/app/calendars-schedule-planner/id608834326).
- [Eventual](https://apps.apple.com/us/app/eventual-calendar/id6756028875) - A personal calendar with layouts explicitly designed for every Duo pose and orientation. [Primary](https://apps.apple.com/us/app/eventual-calendar/id6756028875).
- [Fantastical](https://apps.apple.com/us/app/fantastical-calendar/id718043190) - Create calendar events and tasks in an expanded Duo layout using natural-language input. [Primary](https://apps.apple.com/us/app/fantastical-calendar/id718043190).
- [Finalist](https://apps.apple.com/us/app/finalist-daily-planner/id6447014685) - Open an agenda beside its timeline, or prop Duo like a small laptop for a clock counting down your schedule. [Primary](https://www.finalist.works/4-2/).
- [Portal](https://apps.apple.com/us/app/portal-escape-into-nature/id1436994560) - Unfold into a nature scene, with focus timers, sleep timers and alarms arranged for closed, flat, seated or standing poses. [Primary](https://apps.apple.com/us/app/portal-escape-into-nature/id1436994560).
- [Structured](https://apps.apple.com/us/app/structured-daily-planner-todo/id1499198946) - Run a visual daily plan with a Focus Timer designed for book and tabletop positions. [Primary](https://apps.apple.com/us/app/structured-daily-planner-todo/id1499198946).
- [Things 3](https://apps.apple.com/us/app/things-3/id904237743) - Unfold to reveal a list sidebar, use Split View, and connect a keyboard for the full set of task-management shortcuts. [Primary](https://apps.apple.com/us/app/things-3/id904237743).
- [Tiimo](https://apps.apple.com/si/app/tiimo-daily-to-do-list/id1480220328) - Prop up a visual focus timer beside routine notes and subtasks. [Primary](https://www.apple.com/newsroom/2026/10/developers-bring-incredible-new-app-experiences-to-iphone-duo/).
- [Timepage](https://apps.apple.com/us/app/timepage-calendar-planner/id989178902) - Expand a calendar from the cover display into a wider schedule with Duo-specific vertical navigation. [Primary](https://apps.apple.com/us/app/timepage-calendar-planner/id989178902).

## Reading and research

Feeds, saved articles and visual thinking. Some entries document layout support without a unique hinge interaction.

- [GoodLinks](https://apps.apple.com/ie/app/goodlinks/id1474335294) - Save and annotate reading material in a read-later app whose developer explicitly confirms Duo support. [Primary](https://apps.apple.com/ie/app/goodlinks/id1474335294).
- [Inoreader](https://apps.apple.com/us/app/inoreader-news-rss-reader/id892355414) - Unfold into a feed-and-article workspace without losing your reading position; use its compact layout beside another app. [Primary](https://apps.apple.com/us/app/inoreader-news-rss-reader/id892355414).
- [Instapaper](https://apps.apple.com/us/app/instapaper/id288545208) - A read-later library with a released Duo update and article narration options. [Primary](https://apps.apple.com/us/app/instapaper/id288545208).
- [Xmind](https://apps.apple.com/us/app/xmind-ai-mind-map-brainstorm/id1286983622) - Review an outline alongside its mind map, or open related documents together while developing an idea. [Primary](https://apps.apple.com/us/app/xmind-ai-mind-map-brainstorm/id1286983622).

## Photos and video

Capture, edit, watch and present using the available displays and poses.

- [(Not Boring) Camera](https://apps.apple.com/us/app/not-boring-camera/id6737783441) - Frame photos using the cover-display preview, with a camera interface that fills either screen. [Primary](https://apps.apple.com/us/app/not-boring-camera/id6737783441).
- [Bezel](https://nonstrict.eu/bezel/presskit/2026-10-23-iphone-duo/) - Frame screenshots in Duo poses or animate an unfolding mockup; editing controls move around the hinge on the phone itself. [Primary](https://nonstrict.eu/bezel/presskit/2026-10-23-iphone-duo/).
- [Blackmagic Camera](https://apps.apple.com/us/app/blackmagic-camera/id6449580241) - A professional video camera app with released Duo support; useful when camera control matters more than novelty. [Primary](https://apps.apple.com/us/app/blackmagic-camera/id6449580241).
- [Darkroom](https://apps.apple.com/us/app/darkroom-photo-video-editor/id953286746) - Use the photo editor's iPad-style workflow through an interface responsive to every Duo pose. [Primary](https://apps.apple.com/us/app/darkroom-photo-video-editor/id953286746).
- [Detail](https://apps.apple.com/is/app/detail-ai-video-editor/id1673518618) - Record using the inner, outer or rear camera; send a selfie preview and teleprompter to the cover display, or record both directions in Book Mode. [Primary](https://apps.apple.com/is/app/detail-ai-video-editor/id1673518618).
- [Flipcorder: Retro Camcorder](https://apps.apple.com/us/app/flipcorder-retro-camcorder/id6818168418) - Treat the fold as a camcorder power switch, show subjects a retro preview outside, and close to save a clip. [Primary](https://apps.apple.com/us/app/flipcorder-retro-camcorder/id6818168418).
- [LumaFusion](https://apps.apple.com/us/app/lumafusion/id1062022008) - Edit multitrack video with an interface that adjusts to Duo's different poses and orientations. [Primary](https://apps.apple.com/us/app/lumafusion/id1062022008).
- [Netflix](https://apps.apple.com/us/app/netflix/id363590051) - Watch in book, tent or tabletop poses with playback controls that reposition and a reflection effect that responds to the hinge. [Primary](https://about.netflix.com/en/news/mobile-experience-that-moves-with-you).

## Music and instruments

Turn the hinge into an instrument or the screen into a miniature music player.

- [Aura](https://github.com/adrbn/aura) - Listen to a Navidrome or Subsonic library with playback on one side of the open Duo and lyrics or the queue beside it. Requires a Navidrome or Subsonic server. [Primary](https://github.com/adrbn/aura#every-device) · [Source](https://github.com/adrbn/aura).
- [Deck-Man: Cassette Player](https://apps.apple.com/us/app/deck-man-cassette-player/id6817070335) - Browse music as cassette tapes, insert a tape, and shut the Duo to begin playback. Uses Apple Music or local audio files. [Primary](https://apps.apple.com/us/app/deck-man-cassette-player/id6817070335).
- [Fold Accordion](https://apps.apple.com/us/app/fold-accordion/id6815058989) - Use the hinge as accordion bellows while playing onscreen keys and learning songs. [Primary](https://apps.apple.com/us/app/fold-accordion/id6815058989).
- [Foldissimo – Pocket Accordion](https://apps.apple.com/us/app/foldissimo-pocket-accordion/id6819312842) - Control accordion airflow by folding speed, add vibrato by shaking, and record a tune. [Primary](https://apps.apple.com/us/app/foldissimo-pocket-accordion/id6819312842).
- [Koala Sampler • Beat Maker](https://apps.apple.com/us/app/koala-sampler-beat-maker/id1449584007) - Sample sounds and build beats with a version explicitly updated for Duo. [Primary](https://apps.apple.com/us/app/koala-sampler-beat-maker/id1449584007).
- [MD Vinyl Music App](https://apps.apple.com/us/app/md-vinyl-music-app/id1606306441) - Turn the half-open Duo into a miniature record player with album art above animated vinyl. [Primary](https://apps.apple.com/us/app/md-vinyl-music-app/id1606306441).
- [PianoFold - Rhythm Game](https://apps.apple.com/us/app/pianofold-rhythm-game/id6822806944) - Put the Duo in laptop pose: camera-backed piano tiles approach pads on the lower screen. [Primary](https://apps.apple.com/us/app/pianofold-rhythm-game/id6822806944).

## Games

Fold-controlled games, tabletop boards and documented Duo layout adaptations. Specific hinge mechanics are stated only where sourced.

- [Alibi: Daily Mystery Puzzles](https://apps.apple.com/us/app/alibi-daily-mystery-puzzles/id6790172064) - Open a mystery casebook with a logic board on one page and clues on the other; fold to keep solving outside. [Primary](https://apps.apple.com/us/app/alibi-daily-mystery-puzzles/id6790172064).
- [Battlefleet Duo](https://apps.apple.com/us/app/battlefleet-duo/id6811120963) - Set up a folding naval board with your fleet below and enemy waters upright in front. [Primary](https://apps.apple.com/us/app/battlefleet-duo/id6811120963).
- [Blackbox](https://apps.apple.com/us/app/blackbox/id962969578) - Explore sensor-driven puzzles featured in a roundup of optimized Duo apps. [Reported](https://www.stuff.tv/features/43-iphone-duo-apps-and-games-the-sensible-the-surprising-and-the-gloriously-bonkers/).
- [Calcudoku · Sudoku-like Puzzle](https://apps.apple.com/us/app/calcudoku-sudoku-like-puzzle/id1195710578) - Play arithmetic grid puzzles with documented Split View and Duo support. [Primary](https://apps.apple.com/us/app/calcudoku-sudoku-like-puzzle/id1195710578).
- [Calm Jigsaw: Puzzle for Adults](https://apps.apple.com/us/app/calm-jigsaw-puzzle-for-adults/id6760758340) - Keep the jigsaw board on one half of the open display and the piece tray on the other. [Primary](https://apps.apple.com/us/app/calm-jigsaw-puzzle-for-adults/id6760758340).
- [Catdoku! Cat Logic Puzzles](https://apps.apple.com/us/app/catdoku-cat-logic-puzzles/id6775778251) - Solve cat-placement logic puzzles in a version explicitly updated for Duo. [Primary](https://apps.apple.com/us/app/catdoku-cat-logic-puzzles/id6775778251).
- [Chonky Corgo: Walking RPG](https://apps.apple.com/us/app/chonky-corgo-walking-rpg/id6796920730) - Turn walking into a corgi RPG with a larger Duo view of the adventure. [Primary](https://apps.apple.com/us/app/chonky-corgo-walking-rpg/id6796920730).
- [Delta - Game Emulator](https://apps.apple.com/us/app/delta-game-emulator/id1048524688) - Use pose-aware retro controls and Nintendo DS layouts; close the Duo to put DS games to sleep. [Primary](https://apps.apple.com/us/app/delta-game-emulator/id1048524688).
- [Duometry](https://apps.apple.com/us/app/duometry/id6814650592) - Guess target angles by folding the phone; compete with friends or read the hinge angle. [Primary](https://apps.apple.com/us/app/duometry/id6814650592).
- [Fold Party](https://apps.apple.com/us/app/fold-party/id6820737260) - Pass one phone through party games that use closed, tent, laptop and flat poses. [Primary](https://apps.apple.com/us/app/fold-party/id6820737260).
- [Foldfish](https://apps.apple.com/us/app/foldfish/id6824988199) - Unfold the hinge to prepare a cast, throw the line, and reel fish across a full-width pond. [Primary](https://apps.apple.com/us/app/foldfish/id6824988199).
- [Greens: Mini-golf](https://apps.apple.com/us/app/greens-mini-golf/id6815742588) - Putt on the lower half while a caddie camera shows the course above, or unfold for a full course view. [Primary](https://apps.apple.com/us/app/greens-mini-golf/id6815742588).
- [Hex Armada](https://apps.apple.com/us/app/hex-armada/id6761338531) - Play multiplayer naval combat on a hex map with dedicated Duo and landscape layouts. [Primary](https://apps.apple.com/us/app/hex-armada/id6761338531).
- [Hexiled](https://apps.apple.com/us/app/hexiled/id881274996) - Play a hexagonal word game whose laptop layout places a word constellation on the upright half. [Reported](https://www.stuff.tv/features/43-iphone-duo-apps-and-games-the-sensible-the-surprising-and-the-gloriously-bonkers/).
- [Marbles Unhinged: Folding Maze](https://apps.apple.com/us/app/marbles-unhinged-folding-maze/id6811637729) - Tilt to roll a marble, then bend the hinge to create ramps, walls and drops. [Primary](https://apps.apple.com/us/app/marbles-unhinged-folding-maze/id6811637729).
- [Nitelore](https://apps.apple.com/us/app/nitelore/id6790147739) - Play neon anti-gravity racing with an update that explicitly supports Duo. [Primary](https://apps.apple.com/us/app/nitelore/id6790147739).
- [Nonogram Ultra](https://apps.apple.com/us/app/nonogram-ultra/id6799545084) - Solve picture-logic grids and daily challenges in a Duo-optimized version. [Primary](https://apps.apple.com/us/app/nonogram-ultra/id6799545084).
- [Orisuji](https://apps.apple.com/us/app/orisuji/id6817092898) - Fold a paper maze to join paths, move characters, and continue the combined puzzle on the cover display. [Primary](https://apps.apple.com/us/app/orisuji/id6817092898).
- [Pixelogic - Daily Nonograms](https://apps.apple.com/us/app/pixelogic-daily-nonograms/id318667196) - Solve daily nonograms with an update explicitly adding Duo support. [Primary](https://apps.apple.com/us/app/pixelogic-daily-nonograms/id318667196).
- [Toastie: grilled cheese game](https://apps.apple.com/us/app/toastie-grilled-cheese-game/id6813841355) - Build a sandwich, fold the phone to grill it, and reopen before it burns. [Primary](https://apps.apple.com/us/app/toastie-grilled-cheese-game/id6813841355).
- [Torpedo: Sea Battle 2 Player](https://apps.apple.com/us/app/torpedo-sea-battle-2-player/id6817928839) - Use the half-open phone as a folding sea-battle case or give each board a page in book pose. [Primary](https://apps.apple.com/us/app/torpedo-sea-battle-2-player/id6817928839).
- [Tumble: Gravity Block Puzzle](https://apps.apple.com/us/app/tumble-gravity-block-puzzle/id6810856219) - Separate puzzle board and pieces in book pose, or move touch controls below the fold in laptop pose. [Primary](https://apps.apple.com/us/app/tumble-gravity-block-puzzle/id6810856219).
- [Twofold: Pass & Play](https://apps.apple.com/us/app/twofold-pass-play/id6816330259) - Half-fold to hide a player's board, then close the phone to hand over the next turn privately. [Primary](https://apps.apple.com/us/app/twofold-pass-play/id6816330259).

## Playful objects and art

Small surprises that make the physical shape of the phone part of the experience.

- [ChompDuo](https://apps.apple.com/us/app/chompduo/id6823172460) - Show eyes on the cover, open a monster mouth inside, and fold to make its jaws bite. [Primary](https://apps.apple.com/us/app/chompduo/id6823172460).
- [Fold & Squish: Butterfly Paint](https://apps.apple.com/us/app/fold-squish-butterfly-paint/id6822789179) - Make mirrored paint prints: close the Duo, rub its outer screen, then reopen the painting. [Primary](https://apps.apple.com/us/app/fold-squish-butterfly-paint/id6822789179).
- [kami: hinge driven origami](https://apps.apple.com/us/app/kami-hinge-driven-origami/id6810977836) - Fold virtual paper by moving the phone's hinge, including creases, stacking and reverse folds. [Primary](https://apps.apple.com/us/app/kami-hinge-driven-origami/id6810977836).
- [Lake: Coloring Book for Adults](https://apps.apple.com/us/app/lake-coloring-book-for-adults/id1183717726) - Unfold an adult coloring book into a larger canvas for detailed artwork. [Primary](https://apps.apple.com/us/app/lake-coloring-book-for-adults/id1183717726).
- [Tiny Computers](https://apps.apple.com/app/id6816896250) - Explore ten interactive retro computers with a screen above the fold and keyboard below, including drawing programs and games. A playful recreation rather than a general-purpose operating system. [Primary](https://www.fountaininteractive.com/TinyComputers/press/).

## Fitness and outdoors

Workout dashboards and outdoor tools with documented Duo layouts.

- [Liftin'](https://liftinapp.co/) - Use the partially folded phone to keep a workout routine and the selected exercise's sets visible across the hinge. [Primary](https://liftinapp.co/).
- [Personal Best](https://apps.apple.com/us/app/workout-stats-personal-best/id1510256676) - Replay workouts in a laptop-style seated layout, or inspect activity summaries alongside the workout list. [Primary](https://getpersonalbest.com/duo).
- [Slopes](https://apps.apple.com/it/app/slopes-sci-e-snowboard/id643351983) - Start with a compact ski-tracking interface, then unfold for a much larger trail map. [Primary](https://apps.apple.com/it/app/slopes-sci-e-snowboard/id643351983).
- [SmartGym](https://apps.apple.com/us/app/smartgym-gym-home-workouts/id922744883) - Keep routines beside exercise details in book pose, or prop up a workout with live heart-rate and calorie controls below. [Primary](https://apps.apple.com/us/app/smartgym-gym-home-workouts/id922744883).
- [Wakeout](https://apps.apple.com/us/app/wakeout-fitness-games/id1242116567) - Prop Duo in tent or laptop pose for hands-free workouts; movement games use the half with the camera. [Primary](https://apps.apple.com/us/app/wakeout-fitness-games/id1242116567).

## Weather and nature

Use the expanded display for forecasts, maps and comparisons.

- [CARROT Weather](https://apps.apple.com/us/app/carrot-weather-alerts-radar/id961390574) - Compare weather information using dual-pane radar or multiple windows on the expanded display. [Primary](https://apps.apple.com/us/app/carrot-weather-alerts-radar/id961390574).
- [Mercury Weather](https://apps.apple.com/al/app/mercury-weather/id1621800675) - Unfold to keep saved places beside their forecast, or compare two locations in separate Mercury windows. [Primary](https://apps.apple.com/al/app/mercury-weather/id1621800675).
- [Please Don't Rain](https://apps.apple.com/us/app/please-dont-rain/id6444577668) - Compare weather panels in book pose, or prop Duo like a laptop to jump between forecast charts. [Primary](https://apps.apple.com/us/app/please-dont-rain/id6444577668).
- [Tide Guide](https://apps.apple.com/us/app/tide-guide-charts-tables/id1406371071) - Expand tide charts and lunar details, or inspect weather radar together with tide stations. [Primary](https://apps.apple.com/us/app/tide-guide-charts-tables/id1406371071).

## Travel and navigation

Plan a journey or follow it with layouts that adapt to the phone.

- [Bikemap](https://apps.apple.com/us/app/bikemap-bicycle-tracker-gps/id625759466) - Unfold for a larger cycling-route map, with layouts that adapt when folded or rotated. [Primary](https://apps.apple.com/us/app/bikemap-bicycle-tracker-gps/id625759466).
- [Flighty](https://apps.apple.com/us/app/flighty-live-flight-tracker/id1358823008) - Turn a tray table into a flight-information display by propping Duo in a tent for hands-free journey tracking. [Primary](https://apps.apple.com/us/app/flighty-live-flight-tracker/id1358823008).
- [Tripsy](https://apps.apple.com/us/app/tripsy-travel-planner/id1429967544) - Organize itineraries, trip notes and activity details with navigation and toolbars adapted to Duo. [Primary](https://apps.apple.com/us/app/tripsy-travel-planner/id1429967544).

## Communication

Messages and collaboration with documented Duo support.

- [Airmail](https://apps.apple.com/us/app/airmail-for-gmail-outlook-mail/id993160329) - Keep the inbox visible while reading messages. [Primary](https://www.apple.com/newsroom/2026/10/developers-bring-incredible-new-app-experiences-to-iphone-duo/).

## Cooking and everyday

Everyday workflows made more useful by the folding display.

- [Menu Planner 2](https://www.menu-planner.com/iphone-duo) - Prop a recipe upright above its ingredients and timers, or open flat for a week of meals. [Primary](https://www.menu-planner.com/iphone-duo).

## Source projects and experiments

Buildable projects and prototypes, separate from ordinary downloads. Check each repository for its license, Xcode requirements and test limitations; public source does not necessarily mean an open-source license.

- [Accorduon](https://github.com/artemnovichkov/Accorduon) - Play a virtual accordion whose volume and tone respond to hinge movement, with melody keys on one side and bass buttons on the other. [Primary](https://github.com/artemnovichkov/Accorduon#readme) · Build from source · [Source](https://github.com/artemnovichkov/Accorduon).
- [ClawKit](https://github.com/artemnovichkov/ClawKit) - Turn a half-folded Duo into a miniature claw arcade, with the cabinet above the hinge and joystick controls below. [Primary](https://github.com/artemnovichkov/ClawKit#readme) · Build from source · [Source](https://github.com/artemnovichkov/ClawKit).
- [DuoBird](https://github.com/artemnovichkov/DuoBird) - Steer a bird through gaps by opening the hinge to flap, with touch controls as a fallback. [Primary](https://github.com/artemnovichkov/DuoBird#readme) · Build from source · [Source](https://github.com/artemnovichkov/DuoBird).
- [DuoCut](https://github.com/artemnovichkov/DuoCut) - Move shapes across the crease and fold to slice them in daily, puzzle, and arcade challenges. [Primary](https://github.com/artemnovichkov/DuoCut#readme) · Build from source · [Source](https://github.com/artemnovichkov/DuoCut).
- [Duogami](https://github.com/artemnovichkov/Duogami) - Fold the device to crease virtual origami, follow guided animal lessons, or experiment with a blank sheet. [Primary](https://github.com/artemnovichkov/Duogami#readme) · Build from source · [Source](https://github.com/artemnovichkov/Duogami).
- [DuoRemote](https://github.com/yezzer/DuoRemote) - Mac Screen Sharing client with a laptop pose, trackpad and modifier keys below the fold. Build with Xcode; requires iOS 27.1 and a reachable Mac. [Primary](https://github.com/yezzer/DuoRemote) · Build from source · [Source](https://github.com/yezzer/DuoRemote).
- [Factorio native port](https://github.com/d4m14ndx/factorio-native-arm-ipad) - Run an experimental native Factorio port on Duo with touch, an on-screen keyboard, and Bluetooth keyboard or trackpad controls. Requires a purchased game, compatible Mac and local signing; fold transitions remain untested by its maintainer. [Primary](https://github.com/d4m14ndx/factorio-native-arm-ipad#readme) · Build from source · [Source](https://github.com/d4m14ndx/factorio-native-arm-ipad).
- [FoldRush](https://github.com/AskArtwentythree/foldrush) - Bend the hinge to jump and tilt to steer through a 3D running course. Public source; no root license was found. [Primary](https://github.com/AskArtwentythree/foldrush#readme) · Build from source · [Source](https://github.com/AskArtwentythree/foldrush).
- [Sand Valley](https://github.com/artemnovichkov/SandValley) - Pour virtual sand and fold the phone to send the grains toward the crease. [Primary](https://github.com/artemnovichkov/SandValley#readme) · Build from source · [Source](https://github.com/artemnovichkov/SandValley).
- [SecChain](https://github.com/bannzai/SecChain) - Manage repository secrets and approve paired Mac requests from an iOS companion with layouts captured on Duo's cover and inner displays. [Primary](https://github.com/bannzai/SecChain/pull/88) · Build from source · [Source](https://github.com/bannzai/SecChain).

## Previews and watchlist

Promising ideas whose availability is beta, announced or unconfirmed. A demo or developer claim is not a released feature.

- [Crate Music Library](https://cratemusicapp.com/) - Browse records and liner notes on facing pages, or place playback above the hinge and notes below. [Primary](https://cratemusicapp.com/) · Beta.
- [Crate — iPhone Duo MPC](https://devpost.com/software/crate-iphone-duo-mpc) - Build beats with pads below, performance information above, and hinge-controlled effects. Hackathon prototype; its creators list physical-device testing as future work. [Primary](https://devpost.com/software/crate-iphone-duo-mpc) · Announced.
- [Fold Clock](https://bravely.dev/foldclock) - A planned bedside clock that separates the time from ambient-sound controls when Duo is partially folded. [Primary](https://bravely.dev/foldclock) · Announced.
- [FoldRemote](https://foldremote.app/) - Announced Mac remote client for the Duo opened flat in landscape. Its site says App Store approval is pending and explicitly excludes folded use. [Primary](https://foldremote.app/) · Announced.
- [Takealong](https://takealong.app/index.html) - Preview of Mac remote access with a seated keyboard or trackpad layout. The inspected install button leads to TestFlight despite App Store wording. [Primary](https://takealong.app/index.html) · Beta.

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

### Related repositories

- [Awesome](https://github.com/sindresorhus/awesome) - The original awesome-list ecosystem and conventions.
- [Awesome Mac](https://github.com/jaywcjlove/awesome-mac) - A useful model for organizing end-user software.
- [Awesome iOS](https://github.com/vsouza/awesome-ios) - Libraries and resources for iOS developers.
- [Open-Source iOS Apps](https://github.com/dkhamsing/open-source-ios-apps) - A complementary source-code catalog, including Duo projects.
- [mergisi/awesome-iphone-duo](https://github.com/mergisi/awesome-iphone-duo) - A developer-focused Duo list and sample.
- [Duo development resources](docs/developer-resources.md) - Examples, hinge tools and community simulators.

## Contributing

Found an ingenious app or an inaccurate claim? [Suggest it or send a correction](https://github.com/KeWang0622/awesome-iphone-duo/issues/new/choose). Read the [contribution guide](CONTRIBUTING.md) for evidence requirements and the small local check command.

Original repository content is available under [CC0 1.0](LICENSE). Linked apps and third-party materials retain their own licenses. This is an independent list; the Awesome badge does not imply inclusion in the central directory or endorsement by Apple.
