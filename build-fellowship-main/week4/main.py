from AlgorithmImports import *
from custom_data_source import GbpJpyCustomData

class CustomGbpJpyBacktest(QCAlgorithm):
    def Initialize(self):
        self.SetStartDate(2023, 12, 1)
        self.SetEndDate(2024, 3, 1)
        self.SetCash(100000)

        self.symbol = self.AddData(GbpJpyCustomData, "GBPJPY").Symbol

        # Optimized SMA values for Week 4 (best performer)
        self.fast = self.SMA(self.symbol, 10)
        self.slow = self.SMA(self.symbol, 30)

        # Trend filter
        self.trend = self.SMA(self.symbol, 200)

        # ATR for SL/TP and position sizing
        self.atr = self.ATR(self.symbol, 14)

        self.SetWarmUp(200)

    def OnData(self, data):
        if self.IsWarmingUp:
            return

        if self.symbol not in data:
            return

        price = data[self.symbol].Close
        atr_value = self.atr.Current.Value

        # Trend direction
        if price > self.trend.Current.Value:
            trend_direction = "long"
        elif price < self.trend.Current.Value:
            trend_direction = "short"
        else:
            return

        # ATR-based position sizing (1% risk)
        risk_per_trade = self.Portfolio.Cash * 0.01
        pip_value = 0.01
        position_size = risk_per_trade / (atr_value / pip_value)
        quantity = int(position_size)
        if quantity <= 0:
            return

        # ATR-based SL/TP
        stop_loss_price = price - 2 * atr_value
        take_profit_price = price + 2 * atr_value

        # SMA crossover signals
        long_signal = self.fast.Current.Value > self.slow.Current.Value
        short_signal = self.fast.Current.Value < self.slow.Current.Value

        # Long entry
        if long_signal and trend_direction == "long":
            if not self.Portfolio.Invested:
                self.MarketOrder(self.symbol, quantity)
                self.stopTicket = self.StopMarketOrder(self.symbol, -quantity, stop_loss_price)
                self.limitTicket = self.LimitOrder(self.symbol, -quantity, take_profit_price)

        # Short entry
        elif short_signal and trend_direction == "short":
            if not self.Portfolio.Invested:
                self.MarketOrder(self.symbol, -quantity)
                self.stopTicket = self.StopMarketOrder(self.symbol, quantity, take_profit_price)
                self.limitTicket = self.LimitOrder(self.symbol, quantity, stop_loss_price)

        # Exit if signal disappears
        else:
            if self.Portfolio.Invested:
                self.Liquidate()

