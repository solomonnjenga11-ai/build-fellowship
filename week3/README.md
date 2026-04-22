
# Week 3 — GBPJPY Data Collection, Custom Data Source & Backtesting

## 1. Overview
This Week 3 assignment focuses on collecting GBP/JPY historical data, preparing it for algorithmic trading, creating a custom data source in QuantConnect, and running a backtest using a moving‑average crossover strategy with ATR‑based risk management.  
This work builds directly on Week 1 (data collection) and Week 2 (strategy design).

---

## 2. Data Collection (Google Colab)
Using `yfinance`, I downloaded daily GBPJPY data from 2000–2024.  
The notebook includes:

- Data download using `yfinance`
- Cleaning and formatting (reset index, convert dates, flatten columns)
- Exploratory analysis
- SMA20 and SMA50 calculations
- Golden Cross / Death Cross signal generation
- Export to CSV (`gbpjpy_data.csv`)

This CSV is used as the custom data source in QuantConnect.

---

## 3. Custom Data Source (QuantConnect)
A custom data class (`GbpJpyCustomData`) was created to load the CSV from GitHub.

Key features:
- Reads Date, Open, High, Low, Close
- Sets Close as the primary `Value`
- Integrates with LEAN as a custom data type
- Enables backtesting using my own dataset instead of QC’s built‑in forex data

This fulfills the Week 3 requirement to use a custom data source.

---

## 4. Strategy Description
The strategy combines:

### **Moving‑Average Crossover**
- SMA20 (fast)
- SMA50 (slow)
- Buy when SMA20 crosses above SMA50  
- Sell when SMA20 crosses below SMA50  

This is the same strategy designed in Week 2.

### **ATR‑Based Stop‑Loss & Take‑Profit**
Chosen in Week 2 (Option B):

- ATR(14)
- Stop‑loss = 2 × ATR
- Take‑profit = 2 × ATR

This adds volatility‑aware risk management.

---

## 5. Backtest Results (QuantConnect)
The backtest was run from **Dec 2023 to Mar 2024** using the custom GBPJPY CSV.

### **Key Metrics**
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

### **Included Visuals**
Screenshots (in `/screenshots/`) show:

- Equity curve  
- Metrics summary  
- Rolling statistics  
- Drawdown  
- Exposure  
- Portfolio turnover  

These match the results displayed in QuantConnect.

---

## 6. Limitations
- Only one asset (GBPJPY)
- Short backtest window
- No slippage or fees modeled
- ATR parameters not optimized
- Custom CSV may have limited historical depth

---

## 7. Future Improvements
- Add more currency pairs
- Optimize ATR multipliers
- Add volatility filters
- Add position sizing rules
- Extend dataset to multiple years

---

## 8. Gemini Studio App
A simple Gemini app was deployed to visualize GBPJPY data and allow user interaction.

The link is stored in:
`link_to_app.txt`

---

## 9. Files Included
- `Week3.ipynb` — Data collection and preprocessing  
- `gbpjpy_data.csv` — Cleaned dataset  
- `quantconnect/main.py` — Strategy implementation  
- `quantconnect/custom_data_source.py` — Custom data loader  
- `screenshots/` — Backtest results  
- `link_to_app.txt` — Gemini app link  

End of Week 3 assignment.

