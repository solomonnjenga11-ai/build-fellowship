from AlgorithmImports import *

class GbpJpyCustomData(PythonData):
    def GetSource(self, config, date, isLiveMode):
        # Your verified RAW GitHub link
        url = "https://raw.githubusercontent.com/solomonnjenga11-ai/build-fellowship/refs/heads/main/week3/gbpjpy_data.csv"
        return SubscriptionDataSource(url, SubscriptionTransportMedium.RemoteFile)

    def Reader(self, config, line, date, isLiveMode):
        if not line.strip():
            return None

        data = GbpJpyCustomData()
        data.Symbol = config.Symbol

        try:
            # CSV format:
            # Date,Close,High,Low,Open,Volume
            parts = line.split(",")

            data.Time = datetime.strptime(parts[0], "%Y-%m-%d")
            data.Value = float(parts[1])          # Close price
            data["Close"] = float(parts[1])
            data["High"] = float(parts[2])
            data["Low"] = float(parts[3])
            data["Open"] = float(parts[4])
            data["Volume"] = float(parts[5])

            return data

        except Exception:
            return None
