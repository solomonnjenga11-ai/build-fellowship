# Week 2 -- GBPJPY SMA/ATR Algorithmic Trading Strategy

## Overview

A GBP/JPY hourly SMA 20/50 crossover strategy with a 2x ATR(14) volatility-adjusted stop loss. The algorithm enters long positions when the fast SMA crosses above the slow SMA and short positions when the fast SMA crosses below. ATR is used to size the stop loss distance so the strategy adapts to market volatility. Developed for **Build Fellowship Assignment 1** on the [QuantConnect](https://www.quantconnect.com/) platform.

## Strategy Summary

| Parameter | Value |
|-----------|-------|
| **Asset** | GBP/JPY (Forex) |
| **Timeframe** | Hourly (1H) |
| **Fast SMA** | 20-period |
| **Slow SMA** | 50-period |
| **Stop Loss** | 2x ATR(14) |
| **Backtest Period** | January 2020 -- December 2024 |
| **Starting Capital** | $100,000 |

## Backtest Performance

| Metric | Value |
|--------|-------|
| **Net Profit** | 12.788% |
| **End Equity** | $112,788.19 |
| **Compounding Annual Return** | 2.434% |
| **Sharpe Ratio** | -0.086 |
| **Sortino Ratio** | -0.104 |
| **Max Drawdown** | 13.400% |
| **Win Rate** | 55% |
| **Loss Rate** | 45% |
| **Average Win** | 0.83% |
| **Average Loss** | -0.52% |
| **Profit-Loss Ratio** | 1.60 |
| **Expectancy** | 0.435 |
| **Total Orders** | 118 |
| **Total Fees** | $0.00 |
| **PSR** | 2.179% |

## Risk Metrics

| Metric | Value |
|--------|-------|
| **Alpha** | -0.018 |
| **Beta** | 0.125 |
| **Annual Standard Deviation** | 0.08 |
| **Annual Variance** | 0.006 |
| **Information Ratio** | -0.554 |
| **Tracking Error** | 0.171 |
| **Treynor Ratio** | -0.055 |
| **Drawdown Recovery** | 506 days |
| **Estimated Strategy Capacity** | $1,600,000 |
| **Portfolio Turnover** | 1.72% |

## How It Works

| Step | Description |
|------|-------------|
| **Signal Generation** | Fast SMA(20) and Slow SMA(50) calculated on hourly GBP/JPY data |
| **Long Entry** | When Fast SMA crosses above Slow SMA, enter a long position |
| **Short Entry** | When Fast SMA crosses below Slow SMA, enter a short position |
| **Risk Management** | Stop loss placed at 2x ATR(14) from entry price, adapting to volatility |
| **Position Management** | Existing stop orders are cancelled before new entries |

## Files

| File | Description |
|------|-------------|
| `main.py` | Core algorithm with Initialize() and OnData() methods |
| `README.md` | Strategy documentation and backtest results |

## Tech Stack

| Component | Detail |
|-----------|--------|
| **Platform** | QuantConnect / Lean Engine |
| **Language** | Python |
| **Indicators** | SMA (Simple Moving Average), ATR (Average True Range) |
| **Order Types** | Market Orders, Stop Market Orders |

## Built For

Build Fellowship -- Assignment 1: Modified Moving Average Strategy with Risk Management
