import yfinance
from pandas import DataFrame

SYMBOL_ETH = "ETH-JPY"  # 仮想通貨の銘柄
SYMBOL_BTC = "BTC-JPY"  # 仮想通貨の銘柄
SYMBOLS = [SYMBOL_ETH, SYMBOL_BTC]


def get(symbol: str):
    Ticker = yfinance.Ticker(symbol)
    data = Ticker.history(period="max")
    print(data)
    return data


def toCsv(symbol: str, data: DataFrame):
    fileName = f"yfinace_{symbol}.txt"
    data = data.to_csv(fileName, header=True, index=True, encoding="utf8")
    print(data)


def getAllToCsv():
    for symbol in SYMBOLS:
        data = get(symbol)
        toCsv(symbol, data)
