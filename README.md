# PR #193413 repaired-state native evidence

Retained captures from the repaired native app on iPhone 17 / iOS 27.0 Simulator, synthetic WebSocket RPC fixture, 2026-11-05. Product revision: b2665992303bf4426fb670968540fa9a53c669aa. These are the repaired-state captures, not the issue's unchanged-code control.

- rejected-pin-rows-retained.png: rejected sessions.patch warning together with both loaded conversation rows, no optimistic Pinned state.
- successful-pin-after-navigation.png: after navigating to Synthetic session 2, returning and retrying Pin succeeds; rejection clears, both rows remain, session 2 is open.
- initial-roster-failure-control.png: real roster-load failure still renders Sessions unavailable.
- runtime-proof.txt: retained independent native XCTest result and activity excerpts for opening navigation-2 after rejection and navigation-1 after recovery. One test passed, zero failures/skips. Same test as author run, not an additional unique test.

Synthetic data only; captures visually checked for private data. Runtime excerpt omits local host paths and simulator ID. No physical device, authenticated Gateway, App Store or release-signing claim. Existing full typography and supplemental AdaptiveLayout limitations remain as disclosed in the PR. Evidence-only orphan branch: no changes to PR code or head.
