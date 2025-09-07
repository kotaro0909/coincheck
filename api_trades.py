import json

import ccxt


def get():
    # コインチェックのインスタンスを作成
    exchange = ccxt.coincheck()

    # 取引ペアを指定（例：BTC/JPY）
    symbol = 'BTC/JPY'

    # トレードデータを取得
    trades = exchange.fetch_trades(symbol, limit=10000)
    print(f"count: {len(trades)}")

    json_dat = json.dumps(trades)
    print(json_dat)

    filename = "sample.txt"
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(trades, file, ensure_ascii=False, indent=4)

    # テキストファイルに書き込む基本的な方法
    #content = "Hello, Python!\nこんにちは、Python!"

    #with open(filename, "w", encoding="utf-8") as file:
    #    file.write(json_dat)

    print(f"{filename}にデータを書き込みました。")
