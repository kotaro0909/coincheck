from logging import Formatter, handlers, StreamHandler, getLogger, DEBUG, INFO, FileHandler
from logging.handlers import TimedRotatingFileHandler


def root_logger():
    # root loggerを取得
    logger = getLogger()

    # formatterを作成
    formatter = Formatter('%(asctime)s %(name)s %(funcName)s [%(levelname)s]: %(message)s')
    # filename
    filename = 'test.log'

    # handlerを作成しフォーマッターを設定
    # loggerにhandlerを設定、イベント捕捉のためのレベルを設定
    # log levelを設定
    # stream_handler = StreamHandler()
    # logger.addHandler(stream_handler)
    # stream_handler.setFormatter(formatter)
    # logger.setLevel(DEBUG)

    # ファイル出力ハンドラを設定
    # file_handler = FileHandler(filename)

    # 時間でローテーションするハンドラ
    file_handler = TimedRotatingFileHandler(
        filename, when='D', interval=1, backupCount=5, encoding='utf-8'
    )
    file_handler.setLevel(INFO)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger