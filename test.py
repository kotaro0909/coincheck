import common.db_maria_tx
from api.yfinance import api_yfinance


def test_all():
    test_db()
    test_api_yfinance()


def test_db():
    common.db_maria_tx.test()


def test_api_yfinance():
    api_yfinance.test()
