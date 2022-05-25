import sqlite3


class file_sql:
    def __init__(self):
        """
        Инициализация класса базы данных. Создание таблицы.
        """
        self.con = sqlite3.connect('DB_ht.db')
        self.cur = self.con.cursor()
        self.cur.execute("""CREATE TABLE IF NOT EXISTS tbl(
            id INTEGER PRIMARY KEY,
            name TEXT,
            key TEXT,
            value TEXT);
        """)

    def save_db(self, data):
        """
        Сохранение данных в БД
        :param data: данные
        :return: None
        """
        self.cur.execute("INSERT INTO tbl(name,key,value) VALUES(?,?,?);", data)
        self.con.commit()
        self.con.close()

    def load_db(self, name):
        """
        Загрузка сохранения из БД
        :param name: название сохранения
        :return: results
        """
        conn = sqlite3.connect('DB_ht.db')
        cur = conn.cursor()
        cur.execute(f"SELECT key,value FROM tbl WHERE name = '{name}'")
        results = cur.fetchall()
        return results

    def names(self):
        """
        Вывод сохранений, находящихся в базе данных
        :return: names
        """
        names = []
        conn = sqlite3.connect('DB_ht.db')
        cur = conn.cursor()
        cur.execute(f"SELECT name FROM tbl")
        tmp = cur.fetchall()
        for i in tmp:
            a = i[0]
            names.append(a)
        return names
