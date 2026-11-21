# Project notes

## 01 — Financial performance

The SQL report calculates gross margin, net margin, current ratio, and debt-to-assets for three fictional companies in 2024 and 2025. `NULLIF` prevents division-by-zero errors in the ratio expressions. The financial data is simplified: it is not a complete set of financial statements.

## 02 — Transaction monitoring

Three rules create review alerts: a transaction of at least GBP 10,000, a transaction whose country code is not GB, and three or more transactions by one customer on the same day. Multiple alerts can be raised for the same transaction. The GBP threshold and geographic rule are deliberately illustrative and are not regulatory thresholds or conclusions about suspicious activity.

## 03 — Customer risk

The scoring example adds points for geography, PEP status, ownership complexity, and expected monthly volume. The weights and bands are arbitrary demonstration values. Real customer due diligence depends on verified evidence, context, applicable policy, and human assessment.

## 04 — Sales reporting

Revenue is units multiplied by unit price. Contribution is units multiplied by the difference between unit price and unit cost. Contribution margin divides contribution by revenue. Fixed operating expenses are not included, so contribution should not be interpreted as net profit.

## 05 — ESG indicators

The example compares emissions intensity within each fictional industry and displays employee turnover and board independence. Units and reporting boundaries are simplified. The project does not produce a composite ESG score or predict future sustainability outcomes.

## Running the examples

Use Python 3.9+ and run `python <project-folder>/main.py` from the repository root. Each script writes a SQLite `.db` file beside itself. The HTML files are static explanatory pages. Run `python tests/smoke_test.py` for repeat-execution checks.

## Scope

These examples focus on SQL queries and reproducible Python scripts. They do not include production data pipelines, authentication, interactive charting, statistical validation, or compliance model governance.
