import traceback

import requests
import json

# 記載サンプル
# ticker = api_ticker.ApiTicker(pair.BTC)
# res = ticker.get()
# print(f'res: {res}')


class ApiTicker:
    __pair = ""
    __url_base = "https://coincheck.com"
    __url_ticker = __url_base + "/api/ticker"
    __is_get = False
    __last = 0
    __high = 0
    __low = 0
    __volume = 0
    __timestamp = 0
    __status_code = 0

    def __init__(self, pair: str):
        self.__pair = pair

    def get(self):
        try:
            r = requests.get(self.__url_ticker, params={"pair": self.__pair})

            if r.status_code == 200 or r.reason == 'OK':
                json_dat = json.loads(r.text)
                self.__last = json_dat["last"]
                self.__high = json_dat["bid"]
                self.__high = json_dat["ask"]
                self.__high = json_dat["high"]
                self.__low = json_dat["low"]
                self.__volume = json_dat["volume"]
                self.__timestamp = json_dat["timestamp"]
                self.__status_code = r.status_code
                self.__is_get = True
            else:
                raise f"API接続でエラーが発生しました(statsu:{r.status_code} / reason:{r.reason})"

        except:
            traceback.print_exc()

    def reset(self):
        self.__is_get = False
        self.__last = 0
        self.__high = 0
        self.__low = 0
        self.__volume = 0
        self.__timestamp = 0
        self.__status_code = 0

    def last(self) -> int:
        self.validate()
        return self.__last

    def high(self) -> int:
        self.validate()
        return self.__high

    def low(self) -> int:
        self.validate()
        return self.__low

    def volume(self) -> int:
        self.validate()
        return self.__volume

    def timestamp(self) -> int:
        self.validate()
        return self.__timestamp

    def validate(self) -> bool:
        return self.__is_get
