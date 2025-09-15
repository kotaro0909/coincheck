from logger import logger

import db_maria_tx
import my_logger

if __name__ == '__main__':
    # root loggerを作成
    logger = my_logger.root_logger()
    logger.info('The root logger is created.')

logger.info('main log test')
db = db_maria_tx.test()
