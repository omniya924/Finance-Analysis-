CREATE TABLE IF NOT EXISTS transactions (transaction_id INTEGER PRIMARY KEY, customer_id TEXT, amount_gbp REAL, country TEXT, transaction_time TEXT);
CREATE TABLE IF NOT EXISTS alerts (transaction_id INTEGER, rule TEXT, review_status TEXT DEFAULT 'Pending human review');
