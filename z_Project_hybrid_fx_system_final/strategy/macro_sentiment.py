import json
from pathlib import Path

MACRO_FILE = Path("macro/summary/latest_macro.json")

def load_macro_sentiment():
    """
    Load macro sentiment from a JSON file.
    Returns a dictionary with macro signals.
    """

    if not MACRO_FILE.exists():
        return {"rate_stance": "neutral", "employment": "neutral"}

    with open(MACRO_FILE, "r") as f:
        data = json.load(f)

    return data
