# Hybrid FX Trading System

A multi-signal hybrid forex trading system that fuses technical analysis, machine learning, Hidden Markov Model regime detection, macroeconomic sentiment, and LLM-powered decision-making into a unified strategy for GBP/JPY on the daily timeframe. The system features an end-to-end pipeline — from data acquisition through model training, signal orchestration, backtesting, and performance visualization.

---

## Table of Contents

- [Project Overview](#project-overview)
- [Architecture](#architecture)
- [Folder Structure](#folder-structure)
- [Data Pipeline](#data-pipeline)
- [Model Training](#model-training)
- [Orchestrator Logic](#orchestrator-logic)
- [Backtest Engine](#backtest-engine)
- [Performance Metrics](#performance-metrics)
- [Visualizations](#visualizations)
- [How to Run](#how-to-run)
- [Future Improvements](#future-improvements)
- [License](#license)

---

## Project Overview

**Hybrid FX System** is a quantitative trading framework that takes a *multi-brain* approach to forex trading. Rather than relying on a single model or indicator, it layers five independent signal sources — each capturing a different dimension of market behavior — and merges them through a central orchestrator to produce high-conviction trade decisions.

### Key Highlights

| Capability | Description |
|---|---|
| **5-Signal Fusion** | SMA/ATR technicals, HMM regime detection, ML probability filter, macroeconomic sentiment, and LLM reasoning — all converging in one orchestrator |
| **Regime Awareness** | A Hidden Markov Model classifies the market into distinct regimes (trending, ranging, volatile), allowing the system to adapt its behavior dynamically |
| **LLM Integration** | A large language model layer synthesizes context from all upstream signals to make a final directional judgment |
| **Macro Overlay** | Ingests and summarizes macroeconomic data to align trades with the broader fundamental backdrop |
| **Full Backtest Pipeline** | Vectorized simulation with detailed trade logging, equity tracking, and exported Excel results |
| **Automated Visualization** | Generates equity curves, drawdown charts, regime overlays, and probability distributions |

### Target Instrument

- **Pair:** GBP/JPY
- **Timeframe:** Daily (D1)

---

## Architecture

```text
┌──────────────────────────────────────────────────────────────────┐
│                        DATA LAYER                                │
│   download_data.py → data/processed/gbpjpy_D1.csv               │
└──────────────────────────┬───────────────────────────────────────┘
                           │
                           ▼
┌──────────────────────────────────────────────────────────────────┐
│                      MODEL TRAINING                              │
│   train_models.py → models/hmm/hmm_model.pkl                    │
│                    → models/ml/ml_model.pkl                      │
└──────────────────────────┬───────────────────────────────────────┘
                           │
                           ▼
┌──────────────────────────────────────────────────────────────────┐
│                    STRATEGY SIGNALS                               │
│                                                                  │
│   ┌────────────┐  ┌────────────┐  ┌──────────────────┐           │
│   │  sma_atr   │  │ hmm_regime │  │   ml_filter      │           │
│   │ (Technical)│  │  (Regime)  │  │ (Probability)    │           │
│   └─────┬──────┘  └─────┬──────┘  └────────┬─────────┘           │
│         │               │                  │                     │
│   ┌─────┴───────────┐   │                  │                     │
│   │macro_sentiment  │   │                  │                     │
│   │(Fundamentals)   │   │                  │                     │
│   └─────┬───────────┘   │                  │                     │
│         │               │                  │                     │
│         └───────┬───────┴──────────┬───────┘                     │
│                 │                  │                              │
│                 ▼                  ▼                              │
│         ┌──────────────────────────────┐                         │
│         │       orchestrator.py        │                         │
│         │  (Merges all five signals)   │                         │
│         └──────────────┬───────────────┘                         │
│                        │                                         │
│                        ▼                                         │
│         ┌──────────────────────────────┐                         │
│         │      llm_decision.py         │                         │
│         │  (LLM final judgment call)   │                         │
│         └──────────────┬───────────────┘                         │
└────────────────────────┼─────────────────────────────────────────┘
                         │
                         ▼
┌──────────────────────────────────────────────────────────────────┐
│                     BACKTEST ENGINE                               │
│   backtests/run_backtest.py → backtest_results.xlsx               │
└──────────────────────────┬───────────────────────────────────────┘
                           │
                           ▼
┌──────────────────────────────────────────────────────────────────┐
│                  ANALYSIS & REPORTING                             │
│   analysis/plot_and_metrics.py → analysis/figures/                │
│   (Equity Curve · Drawdown · Regime Overlay · ML Probabilities)  │
└──────────────────────────────────────────────────────────────────┘
Folder Structure
text


Copy
hybrid_fx_system/
│
├── analysis/                          # Performance analysis and visualization
│   ├── figures/                       # Exported chart PNGs
│   │   ├── Figure_1 Equity Curve.png
│   │   ├── Figure_2 Drawdown (%).png
│   │   ├── Figure_3 Price with Regime Overlay.png
│   │   └── Figure_4 ML Probability Distribution.png
│   └── plot_and_metrics.py            # Metrics computation and chart generation
│
├── backtests/                         # Backtesting engine and results
│   ├── __pycache__/
│   │   └── run_backtest.cpython-312.pyc
│   ├── run_backtest.py                # Vectorized backtest simulator
│   └── backtest_results.xlsx          # Exported trade log and summary stats
│
├── data/                              # Raw and processed price data
│   ├── raw/                           # (Empty) Placeholder for original downloads
│   └── processed/
│       └── gbpjpy_D1.csv             # Cleaned GBP/JPY daily OHLCV data
│
├── macro/                             # Macroeconomic data layer
│   └── summary/
│       └── latest_macro.json          # Latest macro sentiment summary
│
├── models/                            # Trained model artifacts
│   ├── hmm/
│   │   └── hmm_model.pkl             # Serialized Hidden Markov Model
│   └── ml/
│       └── ml_model.pkl              # Serialized ML classifier
│
├── strategy/                          # Strategy signal modules
│   ├── __pycache__/
│   │   ├── hmm_regime.cpython-312.pyc
│   │   ├── llm_decision.cpython-312.pyc
│   │   ├── macro_sentiment.cpython-312.pyc
│   │   ├── ml_filter.cpython-312.pyc
│   │   ├── orchestrator.cpython-312.pyc
│   │   └── sma_atr.cpython-312.pyc
│   ├── hmm_regime.py                  # HMM-based market regime classifier
│   ├── llm_decision.py                # LLM-powered final decision layer
│   ├── macro_sentiment.py             # Macro data ingestion and sentiment scoring
│   ├── ml_filter.py                   # ML probability filter for trade validation
│   ├── orchestrator.py                # Central signal fusion and trade decision engine
│   └── sma_atr.py                     # SMA crossover + ATR-based signal generator
│
├── config.py                          # Central configuration (pairs, params, paths)
├── download_data.py                   # Data acquisition script
├── train_models.py                    # HMM and ML model training script
└── README.md                          # Project documentation (this file)
Data Pipeline
The data pipeline acquires, cleans, and prepares GBP/JPY daily price data for consumption by all downstream models and strategies.

Stage 1 — Data Acquisition
download_data.py fetches historical GBP/JPY OHLCV data and stores it in data/processed/.

Retrieves daily candles with Open, High, Low, Close, and Volume fields.

Outputs a clean CSV (gbpjpy_D1.csv) ready for feature computation and model training.

The data/raw/ directory is reserved for original unprocessed downloads.

Stage 2 — Feature Engineering & Indicators
Features are computed on-the-fly within the strategy modules rather than in a separate preprocessing step:

Module	Features Computed
sma_atr.py	Simple Moving Average crossover signals; Average True Range for volatility measurement and stop-loss/take-profit sizing
hmm_regime.py	Latent regime state probabilities derived from returns and volatility sequences
ml_filter.py	Directional probability scores from the trained ML classifier
macro_sentiment.py	Sentiment scores parsed from macro/summary/latest_macro.json


All features use only past and present data — no look-ahead bias.

Model Training
train_models.py trains and serializes both models used by the system.

Hidden Markov Model (HMM)
Purpose: Classifies the market into discrete regimes (e.g., trending, ranging, volatile) based on observable sequences of returns and volatility.

Output: models/hmm/hmm_model.pkl — a serialized HMM used by strategy/hmm_regime.py at inference time to tag each bar with a regime label and state probabilities.

Why HMM: Markets exhibit regime-switching behavior that is not captured by static indicators. The HMM learns latent structure in price dynamics, allowing the orchestrator to adapt strategy behavior to the current market environment.

ML Classifier
Purpose: Predicts the directional probability of the next move (bullish vs. bearish) using engineered features from price data.

Output: models/ml/ml_model.pkl — a serialized classifier used by strategy/ml_filter.py to generate probability-calibrated trade signals.

Training Discipline:

Strict chronological train/test split — no shuffling — to preserve temporal integrity.

No future data leakage — all input features computed from past and present bars only.

Class-weight balancing to handle directional imbalance in the target variable.

Orchestrator Logic
strategy/orchestrator.py is the central brain of the system. It ingests signals from all five upstream modules and synthesizes them into a single trade decision.

Signal Sources
#	Module	Role	Output
1	sma_atr.py	Technical foundation — SMA crossover for direction, ATR for volatility context	Buy/Sell signal + ATR value
2	hmm_regime.py	Market regime classification — identifies whether the market is trending, ranging, or volatile	Regime label + state probabilities
3	ml_filter.py	Probabilistic directional filter — validates technical signals with ML confidence	Directional probability score
4	macro_sentiment.py	Fundamental overlay — aligns trades with the macroeconomic backdrop	Sentiment score (bullish/bearish/neutral)
5	llm_decision.py	Final reasoning layer — LLM synthesizes all upstream context into a judgment	Go / No-Go + reasoning


Decision Flow
text


Copy
SMA/ATR Signal ──────────┐
                         │
HMM Regime Label ────────┤
                         │
ML Probability Score ─────┼──▶  ORCHESTRATOR  ──▶  LLM DECISION  ──▶  TRADE / NO TRADE
                         │     (signal fusion)    (final judgment)
Macro Sentiment Score ────┤
                         │
Config Parameters ────────┘
How the Orchestrator Decides
SMA/ATR generates the base signal — a directional bias (long or short) grounded in trend-following logic, with ATR providing volatility context for position sizing and stop placement.

HMM regime filters the environment — if the market is in an unfavorable regime (e.g., choppy/ranging when a trend signal fires), the orchestrator can suppress the trade.

ML filter validates conviction — the ML probability score acts as a confidence gate; signals below the threshold are discarded.

Macro sentiment provides fundamental alignment — trades that conflict with the prevailing macroeconomic direction are penalized or blocked.

LLM makes the final call — with all upstream signals and context assembled, the LLM layer reasons over the combined picture and issues a final Go / No-Go decision.

Backtest Engine
backtests/run_backtest.py simulates the orchestrator's trade decisions against historical data to evaluate strategy performance before any live deployment.

Features
Vectorized Execution: Efficient NumPy/Pandas-based simulation for fast iteration.

Realistic Cost Modeling: Accounts for spread costs and slippage to approximate real-world execution.

Complete Trade Logging: Every entry and exit is recorded with timestamp, direction, price levels, P&L, and running equity.

Excel Export: Full results are exported to backtests/backtest_results.xlsx for inspection, sharing, and external analysis.

Workflow
Processed data is loaded from data/processed/gbpjpy_D1.csv.

Strategy signals are generated bar-by-bar through the orchestrator pipeline.

The backtest engine simulates fills, tracks open positions with stop-loss and take-profit levels, and logs every trade.

A complete trade log and equity series are written to backtest_results.xlsx.

The equity series and trade log feed into analysis/plot_and_metrics.py for visualization.

Performance Metrics
Backtest results on the primary test period (GBP/JPY Daily):

Metric	Value
Final Equity	1.33
Win Rate	57.52%
Sharpe Ratio	0.46
Max Drawdown	−5.25%
Profit Factor	1.39
Expectancy	0.0023
Total Trades	130


Metric Definitions
Final Equity: Terminal portfolio value normalized to a starting equity of 1.0 — a value of 1.33 represents a 33% return over the test period.

Win Rate: Percentage of trades closed in profit (75 of 130 trades).

Sharpe Ratio: Annualized risk-adjusted return; 0.46 indicates positive but moderate risk-adjusted performance.

Max Drawdown: Largest peak-to-trough equity decline; −5.25% reflects controlled downside risk.

Profit Factor: Gross profits divided by gross losses; values above 1.0 indicate a net-profitable system.

Expectancy: Average dollar return per trade per unit risked; positive expectancy confirms a statistical edge.

Total Trades: 130 trades provides a reasonable sample size for statistical evaluation.

Visualizations
All figures are generated by analysis/plot_and_metrics.py and saved to analysis/figures/.

Figure 1 — Equity Curve
Tracks the cumulative portfolio value over the test period, illustrating the system's growth trajectory, consistency, and drawdown recovery behavior.


Figure 2 — Drawdown (%)
Visualizes the percentage peak-to-trough decline at every point in time, highlighting the depth and duration of risk exposure periods.


Figure 3 — Price with Regime Overlay
Plots GBP/JPY price action with the HMM-detected regime states overlaid as colored background bands, showing how the model classifies different market environments over time.


Figure 4 — ML Probability Distribution
A histogram of the ML model's predicted directional probabilities across all bars, revealing the distribution shape, calibration, and separation between bullish and bearish predictions.


How to Run
Prerequisites
Python 3.12+

pip

Installation
bash


# Clone the repository
git clone https://github.com/solomonnjenga11-ai/hybrid_fx_system.git
cd hybrid_fx_system

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate        # Linux/macOS
venv\Scripts\activate           # Windows

# Install dependencies
pip install -r requirements.txt
Run the Full Pipeline
bash


# Step 1: Download and prepare data
python download_data.py

# Step 2: Train HMM and ML models
python train_models.py

# Step 3: Run the backtest
python backtests/run_backtest.py

# Step 4: Generate performance charts and metrics
python analysis/plot_and_metrics.py
Configuration
Edit config.py to adjust:

Target currency pair and timeframe

SMA window lengths and ATR multiplier

HMM number of hidden states

ML model hyperparameters and probability threshold

Macro sentiment source path and scoring weights

LLM model selection and prompt configuration

Risk management parameters (max risk per trade, stop-loss/take-profit multipliers)

Future Improvements
Area	Planned Enhancement
Multi-Pair Expansion	Extend to a portfolio of correlated and uncorrelated pairs (EUR/JPY, GBP/USD, AUD/JPY) for diversification
Walk-Forward Optimization	Implement rolling walk-forward analysis for adaptive parameter tuning across market regimes
Regime-Adaptive Sizing	Dynamically adjust position sizing and risk parameters based on HMM regime state
Advanced LLM Reasoning	Enhance the LLM layer with chain-of-thought prompting, multi-turn context, and reasoning traces
Live Paper Trading	Connect to a broker API (e.g., OANDA, MetaTrader 5) for real-time paper trading validation
Ensemble ML Models	Experiment with gradient boosting, stacking, and neural architectures for the ML filter
Real-Time Macro Feed	Automate macro data ingestion from economic calendars and news APIs
Dashboard	Build a Streamlit dashboard for real-time monitoring, trade journaling, and interactive analysis
Logging & Alerts	Integrate structured logging and notification alerts (email/Telegram) for signal generation events


License
This project is for educational and research purposes. Not intended as financial advice. Use at your own risk.

Built with Python · NumPy · Pandas · Scikit-learn · hmmlearn · Matplotlib
