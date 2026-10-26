# Turn iPhone Duo into a laptop

Source review: **2026-10-26**. These recipes assemble documented setup steps; **we have not installed the apps or tested Duo hardware**. There are no benchmark or latency claims here. Start with a short task you can verify, such as editing and saving a document, before relying on a setup away from home.

## Choose where the work runs

| Your goal | Route | What actually runs |
| --- | --- | --- |
| Use existing desktop software | [Headroom](https://apps.apple.com/us/app/headroom-remote-desktop/id6790331904), [Farroom](https://farroom.danielren.tz/) | A separate computer runs the applications; Duo supplies the display and input. |
| Browse and work in movable windows | [PXS Desktop](https://apps.apple.com/us/app/pxs-external-screen-desktop/id6756102352) local mode | An iOS workspace with web pages and built-in tools. |
| Boot a guest operating system locally | [UTM SE](https://docs.getutm.app/installation/ios/) | Actual emulation on the phone, with substantial constraints below. |
| Play with miniature retro machines | [Tiny Computers](https://www.fountaininteractive.com/TinyComputers/press/) | Interactive recreations with games and drawing tools; no general-purpose guest-OS installation is documented. |

## Recipe 1: reach your Mac with Headroom

You need a reachable, awake Mac and an account permitted to share its screen. No Headroom companion is required on that Mac.

1. On the Mac, open **System Settings → General → Sharing**, enable **Screen Sharing**, and use its information panel to allow your Mac account. [Apple setup](https://support.apple.com/en-ie/guide/mac-help/mh11848/mac/1000).
2. Put Duo on the same network, open Headroom, choose the discovered Mac, and enter that Mac account's username and password.
3. Half-fold Duo and switch its lower surface between keyboard and trackpad. Try opening, editing, and saving a disposable document on the Mac.

Unlimited connection time requires Pro. For access away from that network, arrange a VPN connection to the Mac. [Headroom requirements and release notes](https://apps.apple.com/us/app/headroom-remote-desktop/id6790331904).

## Recipe 2: reach Windows with Farroom

Built-in RDP hosting requires **Windows Pro, Enterprise, Education, or Windows Server**. Windows Home cannot host it. Keep the host powered on and reachable; enabling access requires administrator rights. [Microsoft requirements](https://learn.microsoft.com/en-us/windows-server/remote/remote-desktop-services/remotepc/remote-desktop-allow-access).

1. On Windows, enable **Settings → System → Remote Desktop** and permit the intended user.
2. On the same network, add an **RDP** computer in Farroom using the host address and account credentials. Use the account password, not a Windows Hello PIN; include a domain when required.
3. Check the server certificate, connect, then test a document edit before leaving the host. [Farroom Windows setup](https://farroom.danielren.tz/support/#windows).

Farroom's Duo layout needs iOS 27.1 and provides lower-half input. Its advertised **eight windows apply to iPad and Mac, not iPhone**. VNC lacks computer audio; Sunshine lacks clipboard sync. These protocols are different choices, not interchangeable feature sets. [Farroom platform and protocol details](https://farroom.danielren.tz/).

## Recipe 3: use a local PXS workspace

1. Install PXS and choose **Open on this screen** on Duo.
2. Open its browser and a built-in tool such as Notes. Sign into any web service you need.
3. Half-fold, enter text with the lower keyboard, then use **Hide Keyboard** to return to the touchpad. Check that your page survives unfolding.

This mode needs no remote computer or PXS account. Web services still need their own connectivity and accounts. Native iOS app shortcuts launch the other app; they do not turn it into an independent PXS window. Access is paid after the trial. [PXS documentation and 1.3.1 notes](https://apps.apple.com/us/app/pxs-external-screen-desktop/id6756102352).

## Local emulation and other requirements

UTM SE needs a guest OS image and configuration. It has **no JIT or hypervisor**; its interpreter targets older or lightweight systems such as DOS or Alpine Linux. [Installation guidance](https://docs.getutm.app/installation/ios/). Version 5.0.8 adds Duo keyboard/touchpad posture support on iOS 27.1. Its macOS graphics features do not establish equivalent iPhone support. [Release notes](https://github.com/utmapp/UTM/releases/tag/v5.0.8).

For alternatives, [Sill](https://github.com/Saffsanity/sill#requirements) requires an Apple silicon Mac running macOS 14+, a companion, and capture/input permissions. [Scry](https://bravely.dev/scry) requires its host app and the same Bravely account on both devices. An SSH client such as [La Terminal](https://apps.apple.com/us/app/la-terminal-mosh-ssh-client/id1629902861) runs development commands on your reachable server; install the tools there.

Browse the [remote desktop catalog](../README.md#tiny-laptops-and-remote-desktops) and [workspaces and terminals](../README.md#desktop-workspaces-and-terminals) for more choices.
