from AlgorithmImports import *

class GbpJpyCustomData(PythonData):
    def GetSource(self, config, date, isLiveMode):
        # Replace with your raw GitHub CSV link
        url = "https://raw.githubusercontent.com/solomonjenga11-ai/build-fellowship/main/week3/gbpjpy_data.csv"
        return SubscriptionDataSource(url, SubscriptionTransportMedium.RemoteFile)

    def Reader(self, config, line, date, isLiveMode):
        if not line.strip():
            return None

        data = GbpJpyCustomData()
        data.Symbol = config.Symbol

        try:
            # CSV format: date,open,high,low,close,volume
            parts = line.split(',')
            data.Time = datetime.strptime(parts[0], "%Y-%m-%d")
            data.Value = float(parts[4])  # close price

            data["open"] = float(parts[1])
            data["high"] = float(parts[2])
            data["low"] = float(parts[3])
            data["close"] = float(parts[4])
            data["volume"] = float(parts[5])

            return data

        except Exception:
            return None

