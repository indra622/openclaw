# Validation and boundaries

The real built UI enters Settings Advanced/Raw and retains synthetic unsaved config `{ "count": 2 }`. The fixture switches actual production build layouts and retires old Activity and toast-view assets (HTTP404). Visible Reload is blocked without changing the draft or document. Before: generic panel-load failure only. After: complete save-or-discard-before-reload message remains visible with Retry/Dismiss.

Visible Dismiss is clicked; explicit discard calls the existing application owner `runtimeConfig.discardDraft` (not a visible Settings Discard click). Visible Reload then loads exactly one new document, retaining `/activity?view=live` and the current build. No config write occurs.

Base failing reproduction: intended missing explanation, one focused case. Final production E2E:2 cases pass (106.60s Vitest, including four fixture builds). Separate focused unit/browser:39 tests pass. UI production/test types, touched lint/format, controller guard, i18n, regression allocation83 and whitespace checks pass. No automated autoreview or hosted approval claimed.

The fixture uses Chromium with service workers blocked and synthetic RPC. This proves the missing-asset user flow, not a live Gateway update, ordinary service-worker frequency or cross-browser behavior. WebKit/Firefox and remote CI are not part of this local result. Raw startup shared chunk grows about0.60kB; rich toast chunks remain lazy. No latency benchmark claim.

SHA256:
- before.png:9070c0312ed425c9adf8dbdd32e1f995fef980c99cdde161da227dc517c70dea
- after.png:adcb3291fe26438b61af1428480646a86cac631a79cdcfbc1d5243e12923f5ef
