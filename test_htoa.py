import unittest
from htoa import HashTable


class HT_test(unittest.TestCase):
    def setUp(self):
        self.ht = HashTable(10)

    def test_put(self):
        for i in range(10):
            self.ht.put(str(i),chr(i+97))
        self.assertEqual(self.ht.all_keys(), ['9', '0', '1', '2', '3', '4', '5', '6', '7', '8'])

    def test_get(self):
        for i in range(10):
            self.ht.put(str(i),chr(i+97))
        self.assertEqual(self.ht.get('0'), 'a')
        self.assertEqual(self.ht.get('6'), 'g')
        self.ht.put('6', 'OK')
        self.assertEqual(self.ht.get('6'), 'OK')

    def test_remove(self):
        for i in range(10):
            self.ht.put(str(i), chr(i+97))
        self.ht.remove('3')
        self.ht.remove('6')
        self.ht.remove('6')
        self.assertEqual(self.ht.all_keys(), ['9', '0', '1', '2', '4', '5', '7', '8'])


if __name__ == '__main__':
    unittest.main()
