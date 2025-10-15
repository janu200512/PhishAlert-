"""Simple PHISHALERT prototype (CLI)
This is a minimal example to show structure — not production-ready.
"""
import csv
from utils.helpers import is_suspicious_url

DATA_FILE = "data/phishing_urls.csv"

def main():
    print("PHISHALERT prototype — scanning sample URLs from", DATA_FILE)
    with open(DATA_FILE, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            url = row.get('url','').strip()
            score = is_suspicious_url(url)
            status = "SUSPICIOUS" if score >= 0.5 else "OK"
            print(f"{url:50}  score={score:.2f}  => {status}")

if __name__ == '__main__':
    main()
