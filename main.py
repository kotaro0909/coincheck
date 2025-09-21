import os

import test
from common import my_logger
from api.coincheck import api_coincheck

if __name__ == '__main__':
    # root loggerを作成
    path = os.getcwd()
    logger = my_logger.root_logger(f'{path}\logs')
    logger.debug('The root logger is created.')

# テストコード実行
test.test_all()
