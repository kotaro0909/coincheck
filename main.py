# This is a sample Python script.
import datetime

import api_coincheck_ticker
import api_coincheck_trades
import api_yfinance
import db_maria
import db_maria_tx
import pair


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')


# api_yfinance.insertAll()

db = db_maria_tx.test()
