# Week 3 — GBP/JPY Data Engineering, Custom Data Source & Backtesting

## 1. Overview
This Week 3 assignment focuses on building a complete data pipeline and backtesting workflow for the GBP/JPY currency pair.  
The work includes:

- Collecting and preprocessing historical FX data  
- Creating a custom data source for QuantConnect’s LEAN engine  
- Implementing a moving‑average crossover strategy with ATR‑based risk management  
- Running a full backtest  
- Deploying an interactive Gemini Studio app to visualize the data and indicators  

This builds directly on Week 1 (data collection) and Week 2 (strategy design).

---

## 2. Data Collection & Preprocessing (Google Colab)
Using **yfinance**, I downloaded daily GBP/JPY data from 2000–2024 and prepared it for algorithmic trading.

### Notebook includes:
- Data download via `yfinance`
- Cleaning and formatting (reset index, convert dates, flatten columns)
- Exploratory analysis
- SMA20 and SMA50 calculations
- Golden Cross / Death Cross signal generation
- Export to CSV (`gbpjpy_data.csv`)

This cleaned CSV is used as the custom data source in QuantConnect.

---

## 3. Custom Data Source (QuantConnect)
I created a custom Python class (`GbpJpyCustomData`) to load my CSV directly from GitHub.

### Key features:
- Reads Date, Open, High, Low, Close  
- Sets Close as the primary `Value`  
- Integrates with LEAN as a custom data type  
- Enables backtesting using my own dataset instead of QC’s built‑in forex data  

This fulfills the Week 3 requirement to use a custom data source.

---

## 4. Strategy Description
The strategy implemented is the same one designed in Week 2.

### Moving‑Average Crossover
- **SMA20** (fast)  
- **SMA50** (slow)  
- **Buy** when SMA20 crosses above SMA50  
- **Sell** when SMA20 crosses below SMA50  

### ATR‑Based Stop‑Loss & Take‑Profit
Chosen in Week 2 (Option B):

- **ATR(14)**  
- **Stop‑loss = 2 × ATR**  
- **Take‑profit = 2 × ATR**  

This adds volatility‑aware risk management.

---

## 5. Backtest Results (QuantConnect)
The backtest was run from **Dec 2023 to Mar 2024** using the custom GBP/JPY dataset.

### Key Metrics
- **Net Profit:** ~2.4%  
- **Equity:** ~$102,405  
- **PSR:** ~73%  
- **Sharpe Ratio:** ~0.43  
- **Compounding Annual Return:** ~10%  
- **Drawdown:** ~1%  
- **Win Rate:** 100%  
- **Total Orders:** 3  
- **Portfolio Turnover:** 3.32%  
- **Alpha:** 0.016  
- **Beta:** -0.002  
- **Treynor Ratio:** -9.025  
- **Information Ratio:** -2.774  

### Included Visuals
Screenshots (in `/screenshots/`) include:

- Equity curve  
- Metrics summary  
- Rolling statistics  
- Drawdown  
- Exposure  
- Portfolio turnover  

These match the results displayed in QuantConnect.

---

## 6. Limitations
- Only one asset (GBP/JPY)  
- Short backtest window  
- No slippage or fees modeled  
- ATR parameters not optimized  
- Custom CSV has limited historical depth  

---

## 7. Future Improvements
- Add more currency pairs  
- Optimize ATR multipliers  
- Add volatility filters  
- Add dynamic position sizing  
- Extend dataset to multiple years  
- Add regime detection or trend filters  

---

## 8. Gemini Studio App (Deployed)
A fully deployed Gemini Studio app visualizes GBP/JPY data with:

- SMA20, SMA50  
- ATR(14)  
- Multi‑timeframe resampling (1H, 4H, Daily)  
- OHLC tooltips  
- Date range selector  
- Risk module (capital, 1% risk, ATR‑based lot sizing)  
- CSV export of visible chart data  
- Elegant Dark theme  

### Live App Link
Stored in:  
`link_to_app.txt`

---

## 9. Files Included
Week3.ipynb                 # Data collection & preprocessing
gbpjpy_data.csv             # Cleaned dataset
quantconnect/main.py        # Strategy implementation
quantconnect/custom_data_source.py   # Custom data loader
screenshots/                # Backtest results
link_to_app.txt             # Gemini app link

---

## End of Week 3 Assignment

