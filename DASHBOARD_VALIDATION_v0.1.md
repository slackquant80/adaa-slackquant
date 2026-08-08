# ADAA Public Research Dashboard — Validation v0.1

## Verdict

**PASS — usable public-research dashboard prototype.**

Branding layer: **ADAA | SlackQuant**. Branding changes do not alter scientific content, source data, calculations, or paper/replication artifacts.

No scientific result is recomputed in the browser. The dashboard reads a generated JavaScript object built only from rights-safe CSVs already contained in `ADAA_Public_Replication_Package_v1.0.zip`.

## Frozen anchors checked

- paper: `ADAA_SSRN_Working_Paper_v1.15_FINAL`
- scientific freeze: v0.34
- public replication: v1.0
- performance sample: 218 months, June 2008–July 2026
- Decision-Space common history: 216 months, July 2008–June 2026
- 2023 strategy-pool five-rule combinations: 4,368
- historical 2023 family-set rank: 735 / 4,368
- historical Decision-Space score: 0.8171374402
- maximum Decision-Space score: 0.8945418809

## Source and project synchronization

`validate_project_sync_v0.1.py` was run in a simulated current project layout containing the canonical v1.15 PDF and the canonical public replication v1.0 ZIP.

- checks: 61
- failures: 0
- all 19 dashboard source CSVs matched the corresponding files inside the public replication ZIP by SHA-256
- dashboard paper download matched the canonical v1.15 PDF by SHA-256
- dashboard replication download matched the canonical v1.0 replication ZIP by SHA-256

## Static and code checks

- `validate_dashboard_v0.1.py`: 34 checks / 0 failures
- JavaScript syntax: PASS (`node --check` for both data and application scripts)
- local references in `index.html`: no missing CSS/JS/image/download targets
- no runtime market-data download, `fetch()`, XHR, API call, or external chart-library dependency
- no TODO/TBD/PLACEHOLDER tokens

## Visual QA

An all-inline render of the same HTML/CSS/JavaScript was exercised in Chromium for both viewports:

- desktop: 1440 × 1000; full-page height 6,581 px
- mobile: 430 × 900; full-page height 10,565 px
- page/console JavaScript errors: 0 / 0
- current sleeve cards rendered: 5
- 16-rule off-diagonal matrix cells rendered: 240
- displayed historical rank: 735 / 4,368
- displayed practitioner-weight gross CAGR: 10.8%

Manual visual inspection of both full-page renders found no clipping, overlap, broken chart, or unusable mobile section. Wide research tables and the 16-rule matrix intentionally retain horizontal scrolling on narrow screens.

## Reader-facing terminology normalization

The frozen replication CSVs predate the final editorial terminology in a few labels. Source bytes are not altered. The interface normalizes only display text so that:

- `ADAA — historical weights` is displayed as **ADAA — practitioner weights**;
- the Figure 5 source field `historical_weight` is displayed as **later practitioner weight**;
- the current sleeve set is explicitly distinguished from the historical 2023 reference set used in Appendix Z2.

This is presentation-only normalization and changes no number.


## Final copy QA

A final visible-text audit found no spelling errors. Three reader-facing consistency residues were corrected without changing any data or scientific result:

- remaining `Historical weights` UI labels -> **Later practitioner weights**;
- decimal ordinal `83.2th percentile` -> **≈83rd percentile**;
- runtime display of `BAA_Aggressive` / `BAA_Balanced` -> spaces instead of underscores.

The validator now guards against regressions in these labels.
