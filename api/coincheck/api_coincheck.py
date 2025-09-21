import datetime
from logging import getLogger
from time import sleep

import requests
import json

import schedule

from common.db_maria_tx import DbMariaTx

SYMBOL_ETH = "eth_jpy"  # 仮想通貨の銘柄
SYMBOL_BTC = "btc_jpy"  # 仮想通貨の銘柄
SYMBOLS = [SYMBOL_ETH, SYMBOL_BTC]

BASE_URL = "https://coincheck.com"


def get_ticker(symbol: str):
    url = BASE_URL + "/api/ticker"
    rtn = requests.get(url, params={"pair": symbol})
    json_dat = json.loads(rtn.text)
    last = json_dat["last"]
    bid = json_dat["bid"]
    ask = json_dat["ask"]
    high = json_dat["high"]
    low = json_dat["low"]
    volume = json_dat["volume"]
    tick_date = datetime.datetime.fromtimestamp(json_dat["timestamp"])
    print(rtn)

    sql_str = "insert into tick_history (" \
              "tick_datetime, symbol, last, bid, ask, high, low, volume" \
              ") " \
              "values (?, ?, ?, ?, ?, ?, ?, ?);"
    params = (tick_date, symbol, last, bid, ask, high, low, volume)

    db = DbMariaTx()
    db.connect()
    db.execute(sql_str, params)
    db.commit()
    db.close()


def all_tick():
    for symbol in SYMBOLS:
        get_ticker(symbol)


def schedule_ticker():
    schedule.every(10).minutes.do(all_tick)
    while True:
        schedule.run_pending()
        sleep(1)

def test_get_ticker():
    schedule_ticker()
