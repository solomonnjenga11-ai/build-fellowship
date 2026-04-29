import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib
from pathlib import Path

MODEL_PATH = Path("models/ml/ml_model.pkl")

def train_ml_filter(df):
    """
    Train a simple Random Forest classifier to predict
    whether the next candle will be bullish (1) or bearish (0).
    """

    df = df.copy()

    # Force numeric conversion (critical)
    cols = ["Close", "High", "Low", "Open", "Volume"]
    for c in cols:
        df[c] = pd.to_numeric(df[c], errors="coerce")

    df["Return"] = df["Close"].pct_change()
    df["Volatility"] = df["Return"].rolling(24).std()
    df["Direction"] = (df["Close"].shift(-1) > df["Close"]).astype(int)

    df = df.dropna()

    features = df[["Return", "Volatility"]]
    labels = df["Direction"]

    X_train, X_test, y_train, y_test = train_test_split(
        features, labels, test_size=0.2, shuffle=False
    )

    model = RandomForestClassifier(
        n_estimators=200,
        max_depth=5,
        random_state=42
    )

    model.fit(X_train, y_train)

    MODEL_PATH.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, MODEL_PATH)

    return model
