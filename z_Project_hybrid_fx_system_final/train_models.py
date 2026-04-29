import pandas as pd
from pathlib import Path

from strategy.hmm_regime import train_hmm
from strategy.ml_filter import train_ml_filter

DATA_FILE = Path("data/processed/gbpjpy_D1.csv")

def main():
    print("Loading data...")
    df = pd.read_csv(DATA_FILE, parse_dates=["Date"], index_col="Date")

    print("Training HMM model...")
    hmm_model = train_hmm(df)
    print("HMM model trained and saved.")

    print("Training ML model...")
    ml_model = train_ml_filter(df)
    print("ML model trained and saved.")

    print("All models trained successfully.")

if __name__ == "__main__":
    main()
