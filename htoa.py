class HashTable(object):

    def __init__(self, size):
        self.slots = [None] * size
        self.data = [None] * size

    def put(self, key, data):
        """
        Добавление элемента и его ключа
        :param key: ключ
        :param data: элемент
        :return: None
        """
        hashvalue = self.hashfunction(key, len(self.slots))

        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else:
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data

            else:
                nextslot = self.rehash(hashvalue, len(self.slots))

                while self.slots[nextslot] != None and self.slots[nextslot] != key:
                    nextslot = self.rehash(nextslot, len(self.slots))

                if self.slots[nextslot] == None:
                    self.slots[nextslot] = key
                    self.data[nextslot] = data
                else:
                    self.data[nextslot] = data

    def hashfunction(self, key, size):
        """
        Хеш-функция
        Реализует простой метод остатков
        :param key: ключ
        :param size: размер таблицы
        :return: hashsum - номер ячейки
        """
        hashsum = 0
        # пербор символов в key
        for idx, c in enumerate(key):
            # добавть (индекс + длина key) ^ (код символа сейчас)
            hashsum += (idx + len(key)) ** ord(c)
            # hashsum сохраняется в пределах [0, self.capacity - 1]
            hashsum = hashsum % size
        return hashsum

    def rehash(self, oldhash, size):
        """
        Итерация по ячейкам
        :param oldhash: старое значение
        :param size: размер таблицы
        :return: следующая ячейка
        """
        return (oldhash + 1) % size

    def get(self, key):
        """
        Поиск элемента по его ключу
        :param key: ключ
        :return: data
        """
        startslot = self.hashfunction(key, len(self.slots))
        data = None
        stop = False
        found = False
        position = startslot

        while not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]

            else:
                position = self.rehash(position, len(self.slots))
                if position == startslot:
                    stop = True
        return data

    def remove(self, key):
        """
        Удаление значения по его ключу
        :param key: ключ
        :return: None
        """
        startslot = self.hashfunction(key, len(self.slots))
        data = None
        stop = False
        found = False
        position = startslot

        while not found and not stop:
            if self.slots[position] == key:
                found = True
                self.slots[position] = None
                self.data[position] = None

            else:
                position = self.rehash(position, len(self.slots))
                if position == startslot:
                    stop = True

    def all_keys(self):
        """
        Вывод всех ключей
        :return: keys
        """
        keys = []
        for key in self.slots:
            if key:
                keys.append(key)
        return keys


if __name__ == "__main__":
    h = HashTable(10)
    h.put('doctor', 1)
    h.put('sir', 2)
    h.put('car', 3)
    h.put('cat', 4)
    h.put('day', 5)
    h.put('doc', 6)
    h.put('sasha', 7)
    h.put('salmon', 8)
    print(h.get('cat'))
    print(h.all_keys())
