import mariadb
import multipledispatch


class DbMaria:
    __username = "root"
    __password = "root"
    __mariadb_host = "localhost"
    __database = "cryptocurrency"
    __conn = None
    __cursor = None
    __has_conn = False
    __start_tran = False

    def connect(self):
        try:
            self.__conn = mariadb.connect(
                user=self.__username,
                password=self.__password,
                host=self.__mariadb_host,
                port=3306,
                database=self.__database
            )
            self.__has_conn = True
        except mariadb.Error as e:
            print(f"データベースエラーが発生しました: {e}")

    def close(self):
        try:
            self.__conn.close()
        except mariadb.Error as e:
            print(f"データベースエラーが発生しました: {e}")
        self.__conn = None
        self.__clear_status()

    def start_tran(self):
        try:
            self.__cursor = self.__conn.cursor()
            self.__start_tran = True
        except mariadb.Error as e:
            print(f"データベースエラーが発生しました: {e}")
            self.__clear_status()

    def commit(self):
        try:
            self.__conn.commit()
            self.__cursor.close()
            self.__start_tran = False
        except mariadb.Error as e:
            print(f"データベースエラーが発生しました: {e}")
            if not self.__cursor.check_closed():
                self.__cursor.close()
            self.close()

    @multipledispatch
    def execute(self, sql: str):
        self.__execute(sql, None)

    @multipledispatch
    def execute(self, sql: str, params: tuple):
        self.__execute(sql, params)

    def __execute(self, sql: str, params: tuple):
        try:
            if params is None:
                self.__cursor.execute(sql)
            else:
                self.__cursor.execute(sql, params)
        except mariadb.Error as e:
            print(f"データベースエラーが発生しました: {e}")
            self.__conn.rollback()

    def __clear_status(self):
        self.__start_tran = False
        self.__has_conn = False
