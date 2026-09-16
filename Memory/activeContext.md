# Objective

rpg-flip provides a `Tosser` that randomly selects from any object exposing
a `SIDES` attribute (coins, eight-balls, custom casts), with multi-toss and
unique-selection modes.

# State

Verified 2026-09-16. master at 89bed52 (2026-02-25, MIT license) plus
today's hygiene commit; public repo pknull/rpg-flip. The 2026-01-16 audit
fixes are in the tree (`Castable` runtime-checkable Protocol, SIDES and
ntoss validation, EightBall duplicate removed, edge-case tests). Suite green
today. Memory reduced to the v2 pair; v1 files, reasoning_bank DB, event
logs and dead hook backups were retired.

# Next

- None scheduled.

# Blockers

- None.
