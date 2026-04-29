import yfinance as yf
import pandas as pd
from pathlib import Path

OUTPUT_FILE = Path("data/processed/gbpjpy_D1.csv")

def download_gbpjpy(start="2008-01-01", end="2024-12-31"):
    print("Downloading GBP/JPY data...")
    df = yf.download("GBPJPY=X", interval="1d", start=start, end=end)

    df = df.reset_index()
    df.rename(columns={
        "Datetime": "Date",
        "Open": "Open",
        "High": "High",
        "Low": "Low",
        "Close": "Close",
        "Volume": "Volume"
    }, inplace=True)

    df.to_csv(OUTPUT_FILE, index=False)
    print(f"Saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    download_gbpjpy()
