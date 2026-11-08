# PR #194927 follow-up proof

Actual production-built Chromium screenshot with synthetic Gateway RPC and service workers disabled, 1440x900. Activity and toast renderer assets return actual HTTP 404. The dirty draft and document are retained; the fallback visibly explains saving or discarding changes before reload. Retry and Dismiss remain available. Explicit discard in the test uses the existing application owner, not a Settings Discard click. No live Gateway upgrade or Firefox/WebKit claim.

Screenshot SHA256: 05434753224d1878bb8153768d3c6ea67eee4826b5d924dca13c08f7c3d215d9.

Exact immutable CI base c61a7c0cf6b72f9c35ad8acdc432e132f4d86a50 performance comparison passes: normalized largest JS gzip 564369 bytes, below unchanged fixed ceiling 564484 bytes. No performance limits changed.

16 focused toast tests pass, with plain-text fallback and original fragment markup restored after Retry. Built dirty-draft flow passes; UI types, touched-file lint/format and controller guard pass.

Test-line ratchet remains failing: clean base 6571160 lines / 6571095 ceiling (65 inherited debt); candidate merge 6571243 / 6571178 (same65 debt), own83 growth equals83 allocation. This is not a green CI claim; no unrelated test removal or budget expansion.
