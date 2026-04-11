# Week 2 -- GBPJPY SMA/ATR Algorithmic Trading Strategy

## Overview

This project implements a **GBP/JPY hourly SMA 20/50 crossover strategy** with a **2x ATR(14) volatility-adjusted stop loss**, developed for **Build Fellowship Assignment 1** on the [QuantConnect](https://www.quantconnect.com/) platform.

The algorithm enters long positions when the fast SMA crosses above the slow SMA and enters short positions when the fast SMA crosses below. ATR is used to size the stop loss distance so the strategy adapts to market volatility.

## Strategy Summary

| Detail | Value |
|---|---|
| **Asset** | GBP/JPY (Forex) |
| **Timeframe** | Hourly (1H) |
| **Fast SMA** | 20-period |
| **Slow SMA** | 50-period |
| **Stop Loss** | 2x ATR(14) |
| **Backtest Period** | January 2020 -- December 2024 |
| **Starting Capital** | $100,000 |

## How It Works

1. **Signal Generation**: The algorithm monitors the SMA(20) and SMA(50) on hourly GBP/JPY data.
2. 2. **Long Entry**: When the fast SMA crosses above the slow SMA, the algorithm enters a long position.
   3. 3. **Short Entry**: When the fast SMA crosses below the slow SMA, the algorithm enters a short position.
      4. 4. **Risk Management**: Each trade is protected by a stop-market order placed at 2x the 14-period ATR from the entry price, adapting to current market volatility.
         5. 5. **Position Management**: Before entering a new trade, any existing stop order is cancelled and replaced.
           
            6. ## Files
           
            7. - `main.py` -- Core algorithm with Initialize() and OnData() methods
               - - `README.md` -- This file
                
                 - ## Tech Stack
                
                 - - **Platform**: QuantConnect / Lean Engine
                   - - **Language**: Python
                     - - **Indicators**: SMA (Simple Moving Average), ATR (Average True Range)
                       - - **Order Types**: Market Orders, Stop Market Orders
                        
                         - ## Built For
                        
                         - Build Fellowship -- Assignment 1: Modified Moving Average Strategy with Risk Management
