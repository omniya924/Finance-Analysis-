# Finance and Business Analytics

A collection of small analytical projects covering financial reporting, transaction monitoring, customer due diligence, sales performance, and ESG indicators.

The projects use Python's built-in `sqlite3` module for data storage and SQL queries. Each folder includes a standalone Python script, a database schema, and a simple HTML reference page.

## Projects

| Folder | Analysis |
| --- | --- |
| [01 — Financial performance](01-financial-performance/) | Gross margin, net margin, liquidity, and leverage across two reporting years |
| [02 — Transaction monitoring](02-aml-transaction-monitoring/) | Rule-based review flags for transaction size, geography, and activity frequency |
| [03 — Customer risk](03-kyc-customer-risk/) | Documented risk factors and a transparent scoring example |
| [04 — Sales reporting](04-business-intelligence/) | Revenue and contribution margin by region |
| [05 — ESG indicators](05-esg-risk-explorer/) | Industry-level comparisons of selected environmental, social, and governance metrics |

## Getting started

Requires Python 3.9 or newer. No packages need to be installed.

```bash
python 01-financial-performance/main.py
python 02-aml-transaction-monitoring/main.py
python 03-kyc-customer-risk/main.py
python 04-business-intelligence/main.py
python 05-esg-risk-explorer/main.py
```

Each command initializes a local SQLite database and prints a report. Running it again replaces the example records rather than duplicating them.

Run the basic checks with:

```bash
python tests/smoke_test.py
```

The `dashboard.html` pages describe the metrics and methods; they are static pages, not live database-connected dashboards.

## Data and assumptions

The records are synthetic and the thresholds and weights are examples, not operational risk models. Transaction alerts require human investigation; a PEP designation does not imply misconduct. ESG measures are not standardized across the sample and are not investment ratings. The examples are not intended for real compliance, credit, or investment decisions.

See [project notes](PORTFOLIO_GUIDE.md) for calculation details and limitations.
