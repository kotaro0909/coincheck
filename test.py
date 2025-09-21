import common.db_maria_tx
from api.yfinance import api_yfinance
from api.coincheck import api_coincheck

def test_all():
    # test_db()
    test_api_cck_rates()


def test_db():
    common.db_maria_tx.test()


def test_api_yfinance():
    # api_yfinance.test_retrieve_data()
    api_yfinance.test_insert_db_all()


def test_api_cck_rates():
    api_coincheck.test_get_ticker()
