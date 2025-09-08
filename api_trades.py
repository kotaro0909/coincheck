import json
from encodings import undefined
from pprint import pprint

import ccxt


# 取引ペアを指定（例：BTC/JPY）
symbol = 'BTC/JPY'


def get():

    # コインチェックのインスタンスを作成
    exchange = ccxt.coincheck()

    # プロパティの出力
    pprint(exchange.features)

    # トレードデータを取得
    trades = exchange.fetch_trades(symbol, limit=1000)

    filename = "sample.txt"
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(trades, file, ensure_ascii=False, indent=4)

    # テキストファイルに書き込む基本的な方法
    #content = "Hello, Python!\nこんにちは、Python!"

    #with open(filename, "w", encoding="utf-8") as file:
    #    file.write(json_dat)

    print(f"{filename}にデータを書き込みました。")

def dump_file(contents):
    filename = "sample.txt"
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(contents, file, ensure_ascii=False, indent=4)
