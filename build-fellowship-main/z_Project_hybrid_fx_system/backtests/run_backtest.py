import pandas as pd
from pathlib import Path

from strategy.orchestrator import run_orchestrator

DATA_FILE = Path("data/processed/gbpjpy_D1.csv")

def run_backtest():
    print("Loading data...")
    df = pd.read_csv(DATA_FILE, parse_dates=["Date"], index_col="Date")

    print("Running orchestrator...")
    df = run_orchestrator(df)

    print("Simulating trades...")
    df["Position"] = df["Decision"].apply(
        lambda x: 1 if x == "TRADE" else 0
    )

    df["Return"] = df["Close"].pct_change()
    df["Strategy_Return"] = df["Position"].shift(1) * df["Return"]

    df["Equity"] = (1 + df["Strategy_Return"]).cumprod()

    print("Backtest complete.")
    print(f"Final equity: {df['Equity'].iloc[-1]:.2f}")

    df.to_csv("backtests/backtest_results.csv")
    print("Saved results to backtests/backtest_results.csv")

if __name__ == "__main__":
    run_backtest()
