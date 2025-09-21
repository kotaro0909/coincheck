import requests

SYMBOL_ETH = "eth_jpy"  # 仮想通貨の銘柄
SYMBOL_BTC = "btc_jpy"  # 仮想通貨の銘柄
SYMBOLS = [SYMBOL_ETH, SYMBOL_BTC]


def get_rate(symbole: str):
    base_ural = "https://coincheck.com"
    rate_url = f"{base_ural}/api/exchange/orders/rate"
    rtn = "test"

    params={'order_type': 'sell', 'pair': f'{symbole}'}
    rtn = requests.get(rate_url, params=params)
    return rtn


def test_rate():
    rtn = get_rate(SYMBOL_ETH)
    print(f"rtn: {rtn}")
