# Architecture Overview

PHISHALERT is a small prototype:
- Input: URLs or email text (CSV samples provided)
- Processing: Simple heuristics + ML model placeholder
- Output: Flagged items and a CLI/optional web API

Future improvements:
- Train a real ML model (features: domain age, WHOIS, lexical, HTML features)
- Add a web UI and REST API
