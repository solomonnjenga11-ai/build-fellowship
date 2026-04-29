from AlgorithmImports import *
from custom_data_source import GbpJpyCustomData

class CustomGbpJpyBacktest(QCAlgorithm):
    def Initialize(self):
        self.SetStartDate(2023, 12, 1)
        self.SetEndDate(2024, 3, 1)
        self.SetCash(100000)

        # Add custom data
        self.symbol = self.AddData(GbpJpyCustomData, "GBPJPY").Symbol

        # Indicators
        self.fast = self.SMA(self.symbol, 20)
        self.slow = self.SMA(self.symbol, 50)
        self.atr = self.ATR(self.symbol, 14)

        self.SetWarmUp(50)

    def OnData(self, data):
        if self.IsWarmingUp:
            return

        if self.symbol not in data:
            return

        price = data[self.symbol].Close
        atr_value = self.atr.Current.Value

        # ATR-based stop-loss and take-profit
        stop_loss_price = price - 2 * atr_value
        take_profit_price = price + 2 * atr_value

        # Entry logic
        if self.fast.Current.Value > self.slow.Current.Value:
            if not self.Portfolio.Invested:
                self.SetHoldings(self.symbol, 1)

                # Create stop-loss and take-profit orders
                quantity = self.Portfolio[self.symbol].Quantity
                self.stopTicket = self.StopMarketOrder(self.symbol, -quantity, stop_loss_price)
                self.limitTicket = self.LimitOrder(self.symbol, -quantity, take_profit_price)

        # Exit logic
        elif self.fast.Current.Value < self.slow.Current.Value:
            if self.Portfolio.Invested:
                self.Liquidate()
