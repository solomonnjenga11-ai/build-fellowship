import pandas as pd

def compute_sma_atr(df, sma_fast=20, sma_slow=50, atr_period=14):
    df["SMA_Fast"] = df["Close"].rolling(sma_fast).mean()
    df["SMA_Slow"] = df["Close"].rolling(sma_slow).mean()

    df["H-L"] = df["High"] - df["Low"]
    df["H-PC"] = (df["High"] - df["Close"].shift(1)).abs()
    df["L-PC"] = (df["Low"] - df["Close"].shift(1)).abs()

    df["TR"] = df[["H-L", "H-PC", "L-PC"]].max(axis=1)
    df["ATR"] = df["TR"].rolling(atr_period).mean()

    df.drop(columns=["H-L", "H-PC", "L-PC", "TR"], inplace=True)

    return df
