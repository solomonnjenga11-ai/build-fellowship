import pandas as pd
import joblib

from strategy.sma_atr import compute_sma_atr
from strategy.ml_filter import train_ml_filter
from strategy.macro_sentiment import load_macro_sentiment
from strategy.llm_decision import llm_decision

HMM_MODEL_PATH = "models/hmm/hmm_model.pkl"
ML_MODEL_PATH = "models/ml/ml_model.pkl"

def run_orchestrator(df):
    """
    Combine all signals into a final decision for each candle.
    """

    df = df.copy()

    # ---------------------------------------------------------
    # 1. Compute SMA + ATR features
    # ---------------------------------------------------------
    df = compute_sma_atr(df)

    # ---------------------------------------------------------
    # 2. Load macro sentiment
    # ---------------------------------------------------------
    macro = load_macro_sentiment()

    # ---------------------------------------------------------
    # 3. Load trained HMM model (DO NOT TRAIN HERE)
    # ---------------------------------------------------------
    hmm_model = joblib.load(HMM_MODEL_PATH)

    # Compute HMM features
    df["Return"] = df["Close"].pct_change()
    df["Volatility"] = df["Return"].rolling(24).std()

    df = df.dropna()

    hmm_features = df[["Return", "Volatility"]].astype(float).values
    df["Regime"] = hmm_model.predict(hmm_features)

    # ---------------------------------------------------------
    # 4. Load trained ML model (DO NOT TRAIN HERE)
    # ---------------------------------------------------------
    ml_model = joblib.load(ML_MODEL_PATH)

    ml_features = df[["Return", "Volatility"]].astype(float)
    df["ML_Prob"] = ml_model.predict_proba(ml_features)[:, 1]

    # ---------------------------------------------------------
    # 5. SMA direction
    # ---------------------------------------------------------
    df["SMA_Signal"] = df.apply(
        lambda row: "long" if row["SMA_Fast"] > row["SMA_Slow"] else "short",
        axis=1
    )

    # ---------------------------------------------------------
    # 6. Final LLM decision
    # ---------------------------------------------------------
    df["Decision"] = df.apply(
        lambda row: llm_decision(
            regime="calm" if row["Regime"] == 2 else
                    "normal" if row["Regime"] == 1 else
                    "shock",
            ml_prob=row["ML_Prob"],
            sma_signal=row["SMA_Signal"],
            volatility=row["Volatility"],
            macro=macro
        ),
        axis=1
    )

    return df
