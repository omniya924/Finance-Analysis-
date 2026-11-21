CREATE TABLE IF NOT EXISTS customers (customer_id TEXT PRIMARY KEY, customer_type TEXT, geography_risk TEXT, pep_status INTEGER, complex_ownership INTEGER, expected_monthly_volume_gbp REAL);
CREATE TABLE IF NOT EXISTS assessments (customer_id TEXT, score INTEGER, tier TEXT, rationale TEXT);
