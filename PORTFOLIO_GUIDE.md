# Finance & Business Analytics Portfolio

Five beginner-to-intermediate demonstration projects combining **SQL**, **Python** and **HTML**. The code is designed to be readable, explainable in interviews, and extendable.

| Project | Business question | Files |
|---|---|---|
| [Financial Performance](01-financial-performance/) | Which companies show stronger margins and liquidity? | SQL schema, Python ratio report, HTML overview |
| [AML Transaction Monitoring](02-aml-transaction-monitoring/) | Which synthetic transactions merit further review? | SQL schema, Python rules, HTML overview |
| [KYC Customer Risk](03-kyc-customer-risk/) | How can illustrative risk factors be documented transparently? | SQL schema, Python scoring, HTML overview |
| [Business Intelligence](04-business-intelligence/) | Which regions generate more revenue and contribution? | SQL schema, Python KPIs, HTML overview |
| [ESG Indicator Explorer](05-esg-risk-explorer/) | How do sample indicators vary within an industry? | SQL schema, Python screening, HTML overview |

## Requirements

Python 3.9+; no third-party packages required. SQLite is included with Python.

## How to run

From the repository root:

```bash
python 01-financial-performance/main.py
python 02-aml-transaction-monitoring/main.py
python 03-kyc-customer-risk/main.py
python 04-business-intelligence/main.py
python 05-esg-risk-explorer/main.py
```

Each script creates a `.db` file in its own folder and prints its results. Open `dashboard.html` in a browser for a **static project overview**. The HTML files are not connected to the database and do not visualize live output.

## Interview discussion ideas

- Explain why `NULLIF` is used in financial ratio denominators.
- Describe why AML monitoring rules produce alerts for review, not proof of misconduct.
- Discuss limitations of a weighted KYC score and the importance of verified evidence and human decisions.
- Distinguish contribution margin from net profit.
- Explain why ESG indicators should be compared within relevant industries and reporting definitions.

## Limitations and next steps

All records are **fictional** and analytical methods are **illustrative**, not validated. Potential next steps include automated tests, real interactive dashboards, data dictionaries, input validation, peer-reviewed AML/KYC methodology, and an expanded ESG modeling workflow. Do not use these outputs for real-world compliance, lending, investment or customer decisions.
