# region imports
from AlgorithmImports import *
# endregion

class GbpJpySmaAtrStrategy(QCAlgorithm):

    def Initialize(self):
        # Backtest settings
        self.SetStartDate(2020, 1, 1)
        self.SetEndDate(2024, 12, 31)
        self.SetCash(100000)

        # Forex pair
        self.symbol = self.AddForex("GBPJPY", Resolution.Hour).Symbol

        # Indicators
        self.fast = self.SMA(self.symbol, 20, Resolution.Hour)
        self.slow = self.SMA(self.symbol, 50, Resolution.Hour)
        self.atr  = self.ATR(self.symbol, 14, MovingAverageType.Simple, Resolution.Hour)

        # Warm-up
        self.SetWarmUp(50, Resolution.Hour)

        # Track previous values for crossover detection
        self.prev_fast = None
        self.prev_slow = None

        # Track stop orders
        self.stopTicket = None

    def OnData(self, data: Slice):
        if self.IsWarmingUp:
            return
        if self.symbol not in data:
            return

        price = data[self.symbol].Close
        fast  = self.fast.Current.Value
        slow  = self.slow.Current.Value
        atr   = self.atr.Current.Value

        if atr == 0:
            return

        # Detect crossovers manually
        long_signal = False
        short_signal = False

        if self.prev_fast is not None and self.prev_slow is not None:
            long_signal  = self.prev_fast <= self.prev_slow and fast > slow
            short_signal = self.prev_fast >= self.prev_slow and fast < slow

        # Update previous values
        self.prev_fast = fast
        self.prev_slow = slow

        quantity = self.CalculateOrderQuantity(self.symbol, 1.0)

        # Cancel existing stop if flipping direction
        if self.stopTicket is not None and self.stopTicket.Status in [
            OrderStatus.Submitted, OrderStatus.PartiallyFilled
        ]:
            self.Transactions.CancelOrder(self.stopTicket.OrderId)
            self.stopTicket = None

        # LONG ENTRY
        if long_signal:
            if self.Portfolio[self.symbol].Quantity <= 0:
                self.MarketOrder(self.symbol, abs(quantity))
                stop_price = price - 2 * atr
                self.stopTicket = self.StopMarketOrder(
                    self.symbol, -abs(quantity), stop_price
                )

        # SHORT ENTRY
        elif short_signal:
            if self.Portfolio[self.symbol].Quantity >= 0:
                self.MarketOrder(self.symbol, -abs(quantity))
                stop_price = price + 2 * atr
                self.stopTicket = self.StopMarketOrder(
                    self.symbol, abs(quantity), stop_price
                )
