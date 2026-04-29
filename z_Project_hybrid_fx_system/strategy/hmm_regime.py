import numpy as np
import pandas as pd
from hmmlearn.hmm import GaussianHMM
import joblib
from pathlib import Path

MODEL_PATH = Path("models/hmm/hmm_model.pkl")

def train_hmm(df, n_states=3):
    """
    Train a 3‑state Gaussian HMM using returns and volatility.
    """

    df = df.copy()

    # Force all price columns to numeric
    cols = ["Close", "High", "Low", "Open", "Volume"]
    for c in cols:
        df[c] = pd.to_numeric(df[c], errors="coerce")

    print(df.dtypes.head())
    print(df.head())


    df["Return"] = df["Close"].pct_change()
    df["Volatility"] = df["Return"].rolling(24).std()

    df = df.dropna()

    features = df[["Return", "Volatility"]].astype(float).values

    model = GaussianHMM(
        n_components=n_states,
        covariance_type="diag",
        n_iter=200
    )

    model.fit(features)

    MODEL_PATH.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, MODEL_PATH)

    return model
