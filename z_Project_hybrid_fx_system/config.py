DATA_PATH = "data"
RAW_PATH = f"{DATA_PATH}/raw"
PROCESSED_PATH = f"{DATA_PATH}/processed"

HMM_MODEL_PATH = "models/hmm/hmm_model.pkl"
ML_MODEL_PATH = "models/ml/ml_model.pkl"

PAIR = "GBPJPY"
TIMEFRAME = "H1"  # base timeframe for features

SMA_FAST = 20
SMA_SLOW = 50
ATR_PERIOD = 14

ML_PROB_THRESHOLD_FULL = 0.6
ML_PROB_THRESHOLD_REDUCED = 0.5
