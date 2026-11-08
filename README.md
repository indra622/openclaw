# Retired-toast explanation: reproducible proof

Source follow-up commit `0c729cfb81e6cbf0bfe810e1a86d1ba06442563b` against prior PRhead `7ac8a2785ad1ba513700a9039bb87b8e67ac6e81`. Reviewed patch SHA256 `dcdf456c8bc9fa2d1c6f7f3ebf9baf2625adc2e4c883ca49ee9b2b53a9e14b7d`.

The exact recorded CI merge is `1dc75172af7d913defc6c693452c1cec2680ee6d`, first parent `c61a7c0cf6b72f9c35ad8acdc432e132f4d86a50`. With these Git objects locally available and a caller-owned external/secure proof root, reproduce the source pairing without changing the working branch:

```sh
git diff 7ac8a2785ad1ba513700a9039bb87b8e67ac6e81 0c729cfb81e6cbf0bfe810e1a86d1ba06442563b --binary > "$PROOF_ROOT/candidate.patch"
git worktree add --detach "$PROOF_ROOT/merge" 1dc75172af7d913defc6c693452c1cec2680ee6d
git -C "$PROOF_ROOT/merge" apply "$PROOF_ROOT/candidate.patch"
pnpm --dir "$PROOF_ROOT/merge" install --frozen-lockfile --store-dir "$PROOF_ROOT/store"
pnpm --dir "$PROOF_ROOT/merge" ui:check-performance:base c61a7c0cf6b72f9c35ad8acdc432e132f4d86a50
```

The complete comparison returned exit0 with existing budgets and variance unchanged. Exact sanitized output line:

```text
  largest ordinary JS: assets/control-ui-boot-shared-DiTGFyXK.js, 551.1 KiB gzip (limit: 551.3 KiB)
```

The checker JSON measured normalized largest JS564369 B; fixed ceiling564484 B; immutable base564565 B and64 B variance. The report-only JSON is supplemental measurement; the complete comparator exit0 is the enforcement proof.

From the follow-up checkout, use the supported Node runner and task-local browser/temp configuration:

```sh
OPENCLAW_VITEST_RUNTIME=node pnpm test ui/src/lib/toast-host.loading.test.ts ui/src/lib/toast-host.loading.browser.test.ts ui/src/lib/toast.browser.test.ts --maxWorkers=1
OPENCLAW_VITEST_RUNTIME=node OPENCLAW_CAPTURE_UI_PROOF=1 OPENCLAW_UI_E2E_ARTIFACT_DIR="$PROOF_ROOT/media" node scripts/run-vitest.mjs run --config test/vitest/vitest.ui-e2e.config.ts --configLoader runner ui/src/e2e/control-ui-stale-build-reload.e2e.test.ts -t 'dirty config: true' --maxWorkers=1
```

Observed:16 focused tests pass; selected built case1 passed/1 filtered. Actual missing Activity/toast assets return404, dirty config and current document survive, the precise explanation is visible, and owner-invoked discard permits exactly one route-preserving reload. Synthetic Gateway RPC is installed; static HTTP handling/built UI are real. No live Gateway upgrade or clicked Settings Discard claim. Current after PNG SHA256 `05434753224d1878bb8153768d3c6ea67eee4826b5d924dca13c08f7c3d215d9`; original before `9070c0312ed425c9adf8dbdd32e1f995fef980c99cdde161da227dc517c70dea`, both1440×900.

Inherited ratchet failure is retained, not waived or called green:

```text
Test lines: 6571160; ceiling: 6571095; over by: 65; net delta: 0. Tree is over the ceiling; this change does not add test lines.
Test lines: 6571243; ceiling: 6571178; over by: 65; net delta: +83.
```

The first is clean CIbase, whose zero-growth case is permitted; the second is the candidate merge with own83 growth/grant and still exit1. Existing CSS/document warnings remain. Remote CI was not rerun by this worker. No performance ceiling/shared scalar/allowance change, local autoreview or external publication is claimed.
