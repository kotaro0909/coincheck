import mariadb

__username = "root"
__password = "root"
__mariadb_host = "localhost"
__database = "cryptocurrency"


def execute(sql: str):
    try:
        conn = mariadb.connect(
            user=__username,
            password=__password,
            host=__mariadb_host,
            port=3306,
            database=__database
        )
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        cur.close()
        conn.close()

    except mariadb.Error as err:
        print(f"An error occurred whilst connecting to MariaDB: {err}")


def execute_with_params(sql: str, params: tuple):
    try:
        conn = mariadb.connect(
            user=__username,
            password=__password,
            host=__mariadb_host,
            port=3306,
            database=__database
        )
        cur = conn.cursor()
        cur.execute(sql, params)
        conn.commit()
        cur.close()
        conn.close()

    except mariadb.Error as err:
        print(f"An error occurred whilst connecting to MariaDB: {err}")
