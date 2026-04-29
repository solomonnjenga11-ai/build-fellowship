from AlgorithmImports import *

class GbpJpyCustomData(PythonData):
    def GetSource(self, config, date, isLiveMode):
        return SubscriptionDataSource(
            "https://raw.githubusercontent.com/solomonnjenga11-ai/build-fellowship/refs/heads/main/week3/gbpjpy_data.csv",
            SubscriptionTransportMedium.RemoteFile
        )

    def Reader(self, config, line, date, isLiveMode):
        if not line or line.startswith("Date"):
            return None

        data = line.split(',')
        obj = GbpJpyCustomData()
        obj.Symbol = config.Symbol

        # CSV format: Date,Close,High,Low,Open,Volume
        obj.Time = datetime.strptime(data[0], "%Y-%m-%d")
        close = float(data[1])
        high = float(data[2])
        low = float(data[3])
        open_ = float(data[4])
        volume = float(data[5])

        obj.Value = close

        obj["Open"] = open_
        obj["High"] = high
        obj["Low"] = low
        obj["Close"] = close
        obj["Volume"] = volume

        return obj
