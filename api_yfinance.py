import datetime

import yfinance
from pandas import DataFrame

import db_maria

# 記載サンプル
# api_yfinance.getAllToCsv()

# print(data.dtypes)
# データ構造
# 1: pen            float64
# 2: High            float64
# 3: Low             float64
# 4: Close           float64
# 5: Volume          int64
# 6: Dividends       float64
# 7: Stock Splits    float64

SYMBOL_ETH = "ETH-JPY"  # 仮想通貨の銘柄
SYMBOL_BTC = "BTC-JPY"  # 仮想通貨の銘柄
SYMBOLS = [SYMBOL_ETH, SYMBOL_BTC]


def get_history(symbol: str):
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
        data = get_history(symbol)
        toCsv(symbol, data)


def insertAll():
    print("Insert - start")
    sql_str = "insert into history ("\
              "symbol, hist_date, open_val, high_val, low_val, close_val, volume"\
              ")"\
              "values (?, ?, ?, ?, ?, ?, ?);"

    db_maria.execute("delete from history")

    for symbol in SYMBOLS:
        is_first = True
        print("Get by Symbol", symbol)
        data = get_history(symbol)

        for row in data.itertuples():
            if is_first:
                is_first = False
            else:
                dt = datetime.datetime(row[0].year, row[0].month, row[0].day, row[0].hour, row[0].minute, row[0].second)
                params = (symbol, dt, row[1], row[2], row[3], row[4], row[5])
                db_maria.execute_with_params(sql_str, params)

    print("Insert - End")


