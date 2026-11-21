"""Illustrative AML transaction-monitoring rules on synthetic records."""
import sqlite3
from pathlib import Path
from collections import Counter
ROOT=Path(__file__).resolve().parent
db=sqlite3.connect(ROOT/"aml.db")
db.executescript((ROOT/"schema.sql").read_text())
db.execute("DELETE FROM transactions")
db.execute("DELETE FROM alerts")
records=[
 (1,"C101",250,"GB","2025-02-01 09:00"),(2,"C101",12000,"GB","2025-02-01 09:05"),
 (3,"C202",850,"FR","2025-02-01 11:00"),(4,"C202",950,"FR","2025-02-01 11:04"),
 (5,"C202",1100,"FR","2025-02-01 11:08"),(6,"C303",150,"GB","2025-02-01 12:00"),
 (7,"C404",2500,"AE","2025-02-01 13:00"),(8,"C101",450,"GB","2025-02-01 14:00")]
db.executemany("INSERT INTO transactions VALUES (?,?,?,?,?)",records)
for txid,customer,amount,country,stamp in records:
    if amount>=10000: db.execute("INSERT INTO alerts(transaction_id,rule) VALUES (?,?)",(txid,"Illustrative high-value threshold"))
    if country!="GB": db.execute("INSERT INTO alerts(transaction_id,rule) VALUES (?,?)",(txid,"Cross-border transfer: contextual review"))
# Velocity: >=3 transactions by the same customer on the same date.
counts=Counter((customer,stamp[:10]) for _,customer,_,_,stamp in records)
for txid,customer,amount,country,stamp in records:
    if counts[(customer,stamp[:10])] >= 3:
        db.execute("INSERT INTO alerts(transaction_id,rule) VALUES (?,?)",(txid,"Same-day transaction velocity"))
db.commit()
for row in db.execute("SELECT a.transaction_id,t.customer_id,a.rule,a.review_status FROM alerts a JOIN transactions t USING(transaction_id) ORDER BY a.transaction_id"):
    print(" | ".join(map(str,row)))
print("Alerts are leads for human review, NOT findings of suspicious activity.")
db.close()
