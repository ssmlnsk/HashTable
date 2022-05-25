import unittest

from PyQt5 import QtCore
from PyQt5.QtTest import QTest

from gui import ThisWindow


class HT_test(unittest.TestCase):
    def setUp(self):
        self.w = ThisWindow()
        self.w.show()

    def test_put(self):
        self.w.linekey.setText('key_1')
        self.w.lineval.setText('val_1')
        QTest.mouseClick(self.w.addb, QtCore.Qt.LeftButton)
        self.w.linekey.setText('key_2')
        self.w.lineval.setText('val_2')
        QTest.mouseClick(self.w.addb, QtCore.Qt.LeftButton)
        self.w.linekey.setText('key_3')
        self.w.lineval.setText('val_3')
        QTest.mouseClick(self.w.addb, QtCore.Qt.LeftButton)

        self.assertEqual(self.w.label.text(), 'key_1, key_2, key_3, ')

    def test_find(self):
        self.w.linekey.setText('key_1')
        self.w.lineval.setText('val_1')
        QTest.mouseClick(self.w.addb, QtCore.Qt.LeftButton)
        self.w.linekey.setText('key_2')
        self.w.lineval.setText('val_2')
        QTest.mouseClick(self.w.addb, QtCore.Qt.LeftButton)
        self.w.linekey.setText('key_3')
        self.w.lineval.setText('val_3')
        QTest.mouseClick(self.w.addb, QtCore.Qt.LeftButton)

        self.w.linekey_2.setText('key_2')
        QTest.mouseClick(self.w.fndb, QtCore.Qt.LeftButton)

        self.assertEqual(self.w.resultl.text(), 'val_2')

    def test_delete(self):
        self.w.linekey.setText('key_1')
        self.w.lineval.setText('val_1')
        QTest.mouseClick(self.w.addb, QtCore.Qt.LeftButton)
        self.w.linekey.setText('key_2')
        self.w.lineval.setText('val_2')
        QTest.mouseClick(self.w.addb, QtCore.Qt.LeftButton)
        self.w.linekey.setText('key_3')
        self.w.lineval.setText('val_3')
        QTest.mouseClick(self.w.addb, QtCore.Qt.LeftButton)

        self.w.linekey_2.setText('key_2')
        QTest.mouseClick(self.w.rmvb, QtCore.Qt.LeftButton)

        self.assertEqual(self.w.label.text(), 'key_1, key_3, ')

    def test_db(self):
        self.w.linekey.setText('key_1')
        self.w.lineval.setText('val_1')
        QTest.mouseClick(self.w.addb, QtCore.Qt.LeftButton)
        self.w.linekey.setText('key_2')
        self.w.lineval.setText('val_2')
        QTest.mouseClick(self.w.addb, QtCore.Qt.LeftButton)
        self.w.linekey.setText('key_3')
        self.w.lineval.setText('val_3')
        QTest.mouseClick(self.w.addb, QtCore.Qt.LeftButton)

        self.w.filel.setText('tmp')
        QTest.mouseClick(self.w.saveb, QtCore.Qt.LeftButton)

        self.w.linekey_2.setText('key_3')
        QTest.mouseClick(self.w.rmvb, QtCore.Qt.LeftButton)

        QTest.mouseClick(self.w.loadb, QtCore.Qt.LeftButton)

        self.assertEqual(self.w.label.text(), 'key_1, key_2, key_3, ')


if __name__ == '__main__':
    unittest.main()
