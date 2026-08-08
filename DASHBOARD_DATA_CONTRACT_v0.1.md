# ADAA Public Research Dashboard — Data Contract v0.1

## Principle

The dashboard is a presentation layer only. It does not re-download market data, re-run strategy rules, optimize weights, or recompute paper results. All displayed research results are read from rights-safe files already included in `ADAA_Public_Replication_Package_v1.0.2.zip`.

## Frozen anchors

- Scientific freeze: v0.34
- Paper: `ADAA_SSRN_Working_Paper_v1.21_FINAL_PUBLIC_RELEASE`
- Public replication: v1.0.2
- Performance simulation: June 2008–July 2026 (218 monthly holding returns)
- Decision-Space common target-weight history: July 2008–June 2026 (216 months)

## Important semantic distinction

The current public ADAA sleeve set is HAA / BAA Aggressive / ADM / FAA / LAA. The Appendix A/Z2 historical 2023 reference set is the documented 2023 five-family composition in the reconstructed 16-rule pool: ADM / BAA Aggressive / BAA Balanced / FAA / LAA. The Z2 ranking is a decision-diversity ranking, not a performance ranking.

## Distribution

`assets/js/data.js` is generated from the copied rights-safe source CSVs under `data/source/`. `DATA_MANIFEST_SHA256.csv` records their hashes and original replication paths. The browser reads the generated JavaScript object so the dashboard also works when `index.html` is opened directly from disk without a web server.

## Public links

- Research dashboard: https://slackquant80.github.io/adaa-slackquant/
- Replication repository: https://github.com/slackquant80/adaa-decision-diversification

## Archival DOI

The immutable replication v1.0.2 release is archived at Zenodo: https://doi.org/10.5281/zenodo.21853533.
