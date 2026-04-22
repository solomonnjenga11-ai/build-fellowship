from AlgorithmImports import *

class GbpJpyCustomData(PythonData):
    def GetSource(self, config, date, isLiveMode):
        return SubscriptionDataSource(
            "https://raw.githubusercontent.com/solomonnjenga11-ai/build-fellowship/main/week3/gbpjpy_data.csv",
            SubscriptionTransportMedium.RemoteFile
        )

    def Reader(self, config, line, date, isLiveMode):
        if not line or line.startswith("Date"):
            return None

        data = line.split(',')
        obj = GbpJpyCustomData()
        obj.Symbol = config.Symbol

        obj.Time = datetime.strptime(data[0], "%Y-%m-%d")
        obj.Value = float(data[4])  # Close price
        obj["Open"] = float(data[1])
        obj["High"] = float(data[2])
        obj["Low"] = float(data[3])
        obj["Close"] = float(data[4])

        return obj
