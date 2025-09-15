from logging import Formatter, StreamHandler, getLogger, DEBUG, INFO
from logging.handlers import TimedRotatingFileHandler


def consoleHandler():
    pass


def root_logger():
    # root loggerを取得
    logger = getLogger()

    # formatterを作成
    formatter = Formatter('%(asctime)s %(name)s:%(lineno)s %(funcName)s [%(levelname)s]: %(message)s')
    # filename
    filename = 'test.log'

    # 例）コンソールに出力するハンドラ
    console_handler = StreamHandler()
    logger.addHandler(console_handler)
    console_handler.setFormatter(formatter)
    logger.setLevel(DEBUG)

    # 例）時間でローテーションするファイルを出力するハンドラ
    file_handler = TimedRotatingFileHandler(
        filename, when='D', interval=1, backupCount=5, encoding='utf-8'
    )
    file_handler.setLevel(INFO)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger
