# 📘 **WEEK 4 — Strategy Improvements & Optimization**  
### *Build Fellowship — GBP/JPY Algorithmic Trading Strategy*  
### *Author: Solomon Mwangi*

---

# 📌 1. **Overview**

This week builds on the Week‑3 SMA crossover strategy by introducing three major improvements:

1. **Trend Filter using SMA200**  
2. **ATR‑Based Stop‑Loss & Take‑Profit**  
3. **ATR‑Based Position Sizing (1% risk per trade)**  

After implementing these enhancements, I performed SMA optimization by testing three different fast/slow SMA combinations:

- **10 / 30**  
- **20 / 50**  
- **50 / 200**

The goal was to determine which configuration performs best on GBP/JPY using my custom CSV data.

---

# 📌 2. **Final Week‑4 Strategy Code**

The final strategy uses the **10/30 SMA combination**, which produced the best performance.

See `main.py` for the full implementation.

---

# 📌 3. **Improvements Implemented**

### ✅ **1. Trend Filter (SMA200)**  
Only take trades in the direction of the long‑term trend.

### ✅ **2. ATR‑Based Stop‑Loss & Take‑Profit**  
SL = price − 2 × ATR  
TP = price + 2 × ATR  

### ✅ **3. ATR‑Based Position Sizing (1% Risk)**  
Position size = risk ÷ ATR distance.

---

# 📌 4. **Optimization Methodology**

I tested three SMA combinations:

| Version | Fast SMA | Slow SMA | Purpose |
|--------|----------|----------|---------|
| **A** | 10 | 30 | Fast, responsive |
| **B** | 20 | 50 | Medium speed |
| **C** | 50 | 200 | Long‑term trend |

All versions used:

- Same trend filter  
- Same ATR SL/TP  
- Same ATR position sizing  
- Same custom GBP/JPY CSV  
- Same backtest window (Dec 1, 2023 → Mar 1, 2024)

---

# 📌 5. **Optimization Results**

### ⭐ **A. SMA 10/30 — Best Performer**
- **CAGR: +0.1%**  
- **Drawdown: 0.0%**  
- **Probabilistic Sharpe: 44%**  
- **Trades per day: 0.2**  

**Interpretation:**  
Fast enough to catch small swings in a sideways market.  
Only configuration with a positive return.

---

### ⭐ **B. SMA 20/50 — Underperformed**
- **CAGR: 0.0%**  
- **Probabilistic Sharpe: 16%**  
- **Negative returns per trade**

**Interpretation:**  
Too slow for this choppy period.

---

### ⭐ **C. SMA 50/200 — No Real Trades**
- **CAGR: 0.0%**  
- **Drawdown: 0.0%**  
- **Very few trades**

**Interpretation:**  
GBP/JPY had no major trend shifts during this window.

---

# 📌 6. **Final Chosen Configuration**

### 🎯 **Winner: SMA 10/30**

This version:

- Produced the best return  
- Had zero drawdown  
- Was stable and consistent  
- Worked well with ATR sizing and trend filter  

This is the final Week‑4 strategy.

---

# 📌 7. **Deliverables Included in Week‑4 Folder**

```
week4/
│
├── main.py
├── custom_data_source.py
│
├── 10_30_strategy.pdf
├── 20_50_strategy.pdf
├── 50_200_strategy.pdf
│
└── README.md
```

---

# 📌 8. **Conclusion**

Week‑4 successfully improved the strategy by adding volatility‑aware risk management and a trend filter.  
Optimization showed that **10/30 SMA** is the best configuration for this market regime.


