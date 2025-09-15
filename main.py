import json
import logging
from logging import config

from logger import logger

import db_maria_tx
import my_logger


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


if __name__ == '__main__':
    # root loggerを作成
    logger = my_logger.root_logger()
    logger.info('The root logger is created.')
    print_hi('PyCharm')

logger.info('main log test')
db = db_maria_tx.test()
