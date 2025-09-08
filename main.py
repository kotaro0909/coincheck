# This is a sample Python script.
import api_ticker
import api_trades
import api_yfinance
import pair


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

#ticker = api_ticker.ApiTicker(pair.BTC)
#res = ticker.get()
#print(f'res: {res}')

#api_trades.get()

api_yfinance.getAllToCsv()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
