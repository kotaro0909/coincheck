import logging
from logging import config, getLogger, NullHandler, DEBUG

import mariadb
import multipledispatch


class DbMariaTx:
    __username = "root"
    __password = "root"
    __mariadb_host = "localhost"
    __database = "cryptocurrency"
    __conn = None
    __cursor = None
    _logger = None

    def __init__(self):
        # config.dictConfig(main.log_conf)
        self._logger = getLogger(__name__)
        self._logger.addHandler(NullHandler())
        self._logger.setLevel(DEBUG)
        self._logger.propagate = True
        # self._logger.info("maria-tx init log test")
        print("init finished")

    def connect(self):
        try:
            self.__conn = mariadb.connect(
                user=self.__username,
                password=self.__password,
                host=self.__mariadb_host,
                port=3306,
                database=self.__database
            )
            self._logger.info('connect finished')
        except mariadb.Error as e:
            print(f"データベースエラーが発生しました: {e}")
            raise e

    def close(self):
        try:
            if not self.__cursor.check_closed():
                self.__cursor.close()
            self.__conn.close()
        except mariadb.Error as e:
            print(f"データベースエラーが発生しました: {e}")
            raise e
        self.__conn = None

    def get_rows(self):
        try:
            rows = self.__cursor.fetchall()
            return rows
        except mariadb.Error as e:
            print(f"データベースエラーが発生しました: {e}")
            self.close()
            raise e

    def commit(self):
        try:
            self.__conn.commit()
        except mariadb.Error as e:
            print(f"データベースエラーが発生しました: {e}")
            self.close()
            raise e

    def rollback(self):
        try:
            self.__conn.rollback()
        except mariadb.Error as e:
            print(f"データベースエラーが発生しました: {e}")
            self.close()
            raise e

    @multipledispatch.dispatch()
    def execute(self, sql: str):
        self.__execute(sql, None)

    @multipledispatch.dispatch()
    def execute(self, sql: str, params: tuple):
        self.__execute(sql, params)

    def __execute(self, sql: str, params: tuple):
        try:
            self.__cursor = self.__conn.cursor()
        except mariadb.Error as e:
            print(f"データベースエラーが発生しました: {e}")
            raise e

        try:
            if params is None:
                self.__cursor.execute(sql)
            else:
                self.__cursor.execute(sql, params)
        except mariadb.Error as e:
            print(f"データベースエラーが発生しました: {e}")
            self.__conn.rollback()
            self.close()
            raise e


def test():
    logger = getLogger(__name__)
    logger.addHandler(NullHandler())
    logger.setLevel(DEBUG)
    logger.propagate = True

    db = DbMariaTx()
    db.connect()
    db.execute("delete from test")
    db.commit()
    db.close()

    db.connect()
    db.execute("insert into test(id, text) values (1, 'Hello')")
    db.commit()
    db.close()

    db.connect()
    db.execute("insert into test(id, text) values (?, ?)", (2, "Bye"))
    db.commit()
    db.close()

    db.connect()
    db.execute("insert into test(id, text) values (?, ?)", (3, "Morning"))
    db.execute("select * from test")
    rows = db.get_rows()
    # print(rows)
    logger.info(rows)
    db.rollback()
    db.close()

    db.connect()
    db.execute("insert into test(id, text) values (4, 'Afternoon')")
    db.execute("insert into test(id, text) values (5, 'Evening')")
    db.commit()
    db.close()

    db.connect()
    db.execute("select * from test")
    rows = db.get_rows()
    # print(rows)
    logger.info(rows)
    db.close()
