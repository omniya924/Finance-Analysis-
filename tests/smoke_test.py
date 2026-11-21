"""Run each project twice and check that its report is produced."""
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
PROJECTS = {
    "01-financial-performance": "Gross margin %",
    "02-aml-transaction-monitoring": "Pending human review",
    "03-kyc-customer-risk": "C303",
    "04-business-intelligence": "Contribution margin %",
    "05-esg-risk-explorer": "Within-industry comparison",
}

def main():
    for folder, expected in PROJECTS.items():
        script = ROOT / folder / "main.py"
        for attempt in (1, 2):
            result = subprocess.run(
                [sys.executable, str(script)],
                capture_output=True, text=True, check=False,
            )
            if result.returncode != 0:
                raise AssertionError(f"{folder}, run {attempt}: {result.stderr}")
            if expected not in result.stdout:
                raise AssertionError(f"{folder}, run {attempt}: expected output missing")
        print(f"PASS {folder} (2 runs)")
    print("All smoke tests passed.")

if __name__ == "__main__":
    main()
