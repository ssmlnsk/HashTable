import sys
import ast
from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QApplication, QMessageBox

from htoa import HashTable
from sqldb import file_sql


class ThisWindow(QWidget):
    """
    Класс главного окна
    """
    def __init__(self):
        """
        Инициализация окна, назначение кнопкам функций
        """
        super().__init__()
        uic.loadUi('main_gui.ui', self)
        self.htable = HashTable(50)
        self.addb.clicked.connect(self.put_it)
        self.rmvb.clicked.connect(self.rem_it)
        self.fndb.clicked.connect(self.get_it)
        self.saveb.clicked.connect(self.save)
        self.loadb.clicked.connect(self.load)

    def update(self):
        """
        Обновление списка ключей
        :return: None
        """
        txt = self.htable.all_keys()
        res = ''
        for w in txt:
            res += w+", "
        self.label.setText(res)

    def save(self):
        """
        Сохранение данных в базу данных
        :return: None
        """
        keys = self.htable.all_keys()
        data = []
        name = self.filel.text()
        for k in keys:
            data.append(self.htable.get(k))
        file_sql().save_db((name, str(keys), str(data)))

    def load(self):
        """
        Выгрузка данных в приложение из базы данных
        :return: None
        """
        names = file_sql().names()
        name = self.filel.text()
        if name not in names:
            self.warning_load()
        else:
            data = file_sql().load_db(name)[0]
            keys = ast.literal_eval(data[0])
            data = ast.literal_eval(data[1])
            self.htable = HashTable(50)
            for k, d in zip(keys, data):
                self.htable.put(k, d)
            self.update()

    def warning_load(self):
        """
        Создание MessageBox
        :return: None
        """
        messagebox = QMessageBox(self)
        messagebox.setWindowTitle("Ошибка")
        messagebox.setText("Такого сохранения не существует!")
        messagebox.setIcon(QMessageBox.Warning)
        messagebox.setStandardButtons(QMessageBox.Ok)

        messagebox.show()

    def get_it(self):
        """
        Поиск данных по ключу
        :return: None
        """
        k = self.linekey_2.text()
        res = self.htable.get(k)
        if res:
            self.resultl.setText(res)
        else:
            self.resultl.setText('Нет данных')

    def put_it(self):
        """
        Добавление элемента и его ключа
        :return: None
        """
        k = self.linekey.text()
        v = self.lineval.text()
        self.htable.put(k, v)
        self.update()

    def rem_it(self):
        """
        Удаление элемента по его ключу
        :return: None
        """
        keys = self.htable.all_keys()
        k = self.linekey_2.text()
        if k not in keys:
            self.warning_key()
        else:
            self.htable.remove(k)
            self.update()

    def warning_key(self):
        """
        Создание MessageBox
        :return: None
        """
        messagebox = QMessageBox(self)
        messagebox.setWindowTitle("Ошибка")
        messagebox.setText("Такого элемента нет!")
        messagebox.setIcon(QMessageBox.Warning)
        messagebox.setStandardButtons(QMessageBox.Ok)
        messagebox.show()


app = QApplication(sys.argv)
if __name__ == "__main__":
    w = ThisWindow()
    w.show()
    sys.exit(app.exec_())
