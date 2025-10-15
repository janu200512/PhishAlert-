# Simple helper functions for PHISHALERT demo
import re
def is_suspicious_url(url: str) -> float:
    """Return a simple heuristic score 0.0-1.0 for suspiciousness."""
    if not url:
        return 0.0
    score = 0.0
    # heuristic checks
    if 'login' in url or 'verify' in url or 'secure' in url:
        score += 0.4
    if re.search(r'@[A-Za-z0-9.-]+', url):
        score += 0.3
    if len(url) > 60:
        score += 0.2
    if url.count('-') > 3:
        score += 0.1
    return min(1.0, score)
