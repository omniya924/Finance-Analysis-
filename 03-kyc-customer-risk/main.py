"""Transparent, fictional KYC risk-score exercise."""
import sqlite3
from pathlib import Path
ROOT=Path(__file__).resolve().parent
db=sqlite3.connect(ROOT/"kyc.db")
db.executescript((ROOT/"schema.sql").read_text())
db.execute("DELETE FROM customers");db.execute("DELETE FROM assessments")
records=[
 ("C101","individual","low",0,0,2200),
 ("C202","business","medium",0,1,45000),
 ("C303","individual","high",1,0,8500),
 ("C404","business","low",0,0,12000),
]
db.executemany("INSERT INTO customers VALUES (?,?,?,?,?,?)",records)
for cid,kind,geo,pep,complex_owner,volume in records:
    parts={"geography": {"low":0,"medium":20,"high":40}[geo],
           "PEP":30 if pep else 0,
           "complex ownership":20 if complex_owner else 0,
           "high expected volume":10 if volume>30000 else 0}
    score=sum(parts.values())
    tier="High" if score>=50 else "Medium" if score>=20 else "Low"
    reason=", ".join(f"{k} +{v}" for k,v in parts.items() if v) or "No scored factors"
    db.execute("INSERT INTO assessments VALUES (?,?,?,?)",(cid,score,tier,reason))
db.commit()
for row in db.execute("SELECT * FROM assessments ORDER BY score DESC"): print(" | ".join(map(str,row)))
print("Fictional training scores; never use for actual customer acceptance or de-risking.")
db.close()
