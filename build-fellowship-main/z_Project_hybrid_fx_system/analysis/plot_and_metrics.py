import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load backtest results
df = pd.read_csv("backtests/backtest_results.csv", parse_dates=["Date"], index_col="Date")

# ============================
# 1. EQUITY CURVE PLOT
# ============================

plt.figure(figsize=(14, 6))
plt.plot(df["Equity"], label="Equity Curve", color="blue")
plt.title("Equity Curve")
plt.xlabel("Date")
plt.ylabel("Equity")
plt.grid(True)
plt.legend()
plt.show()

# ============================
# 2. DRAWDOWN PLOT
# ============================

df["Peak"] = df["Equity"].cummax()
df["Drawdown"] = df["Equity"] / df["Peak"] - 1

plt.figure(figsize=(14, 4))
plt.plot(df["Drawdown"], label="Drawdown", color="red")
plt.title("Drawdown (%)")
plt.xlabel("Date")
plt.ylabel("Drawdown")
plt.grid(True)
plt.legend()
plt.show()

# ============================
# 3. REGIME OVERLAY
# ============================

plt.figure(figsize=(14, 6))
plt.plot(df["Close"], label="Price", color="black", alpha=0.6)

colors = {0: "red", 1: "orange", 2: "green"}
for regime in df["Regime"].unique():
    plt.scatter(df.index[df["Regime"] == regime],
                df["Close"][df["Regime"] == regime],
                label=f"Regime {regime}",
                s=10,
                color=colors.get(regime, "gray"))

plt.title("Price with Regime Overlay")
plt.xlabel("Date")
plt.ylabel("Price")
plt.legend()
plt.grid(True)
plt.show()

# ============================
# 4. ML PROBABILITY DISTRIBUTION
# ============================

plt.figure(figsize=(10, 5))
plt.hist(df["ML_Prob"], bins=30, color="purple", alpha=0.7)
plt.title("ML Probability Distribution")
plt.xlabel("Probability")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()

# ============================
# 5. PERFORMANCE METRICS
# ============================

# Trade count
trade_count = (df["Position"].diff().abs() == 1).sum()

# Win rate
wins = (df["Strategy_Return"] > 0).sum()
losses = (df["Strategy_Return"] < 0).sum()
win_rate = wins / max(1, (wins + losses))

# Sharpe ratio
daily_ret = df["Strategy_Return"].fillna(0)
sharpe = np.sqrt(252) * daily_ret.mean() / daily_ret.std() if daily_ret.std() != 0 else 0

# Max drawdown
max_dd = df["Drawdown"].min()

# Profit factor
gross_profit = df[df["Strategy_Return"] > 0]["Strategy_Return"].sum()
gross_loss = df[df["Strategy_Return"] < 0]["Strategy_Return"].sum()
profit_factor = gross_profit / abs(gross_loss) if gross_loss != 0 else np.inf

# Expectancy
expectancy = (gross_profit + gross_loss) / max(1, trade_count)

# Print results
print("\n===== PERFORMANCE METRICS =====")
print(f"Final Equity: {df['Equity'].iloc[-1]:.2f}")
print(f"Trade Count: {trade_count}")
print(f"Win Rate: {win_rate:.2%}")
print(f"Sharpe Ratio: {sharpe:.2f}")
print(f"Max Drawdown: {max_dd:.2%}")
print(f"Profit Factor: {profit_factor:.2f}")
print(f"Expectancy per Trade: {expectancy:.4f}")
