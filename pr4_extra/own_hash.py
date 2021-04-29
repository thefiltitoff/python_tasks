"""
Реализуйте свою структуру данных, хэш-таблицу, аналог встроенного dict.
Используйте функцию hash.
Примените тестирование на случайных данных с использованием assert и dict.
Реализуйте методы чтения, записи, получения размера хэш-таблицы.
Сделайте вышеупомянутые методы стандартными операторами/функциями, по аналогии с dict.
Реализуйте поддержку для цикла for.
"""

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    def __init__(self, capacity=50):
        self.capacity = capacity
        self.size = 0
        self.buckets = [None] * self.capacity
        self.b = 0
        self.n = 0

    def hash(self, key):
        return hash(key) % self.capacity

    def get(self, key):
        index = self.hash(key)
        node = self.buckets[index]

        while node is not None and node.key != key:
            node = node.next

        if node is None:
            return None
        else:
            return node.value

    def __getitem__(self, key):
        return self.get(key)

    def add(self, key, value):
        self.size += 1
        index = self.hash(key)
        node = self.buckets[index]

        if node is None:
            self.buckets[index] = Node(key, value)
            return

        while node.next is not None:
            node = node.next

        node.next = Node(key, value)

    def __setitem__(self, key, value):
        return self.add(key, value)

    def remove(self, key):
        index = self.hash(key)
        node = self.buckets[index]
        prev = None

        while node is not None and node.key != key:
            prev = node
            node = node.next

        if node is None:
            return None

        result = node.value

        if prev is None:
            self.buckets[index] = node.next
        else:
            prev.next = prev.next.next

        self.size -= 1
        return result

    def size(self):
        return self.size

    def __len__(self):
        return self.size

    def __iter__(self):
        self.b = 0
        self.n = self.buckets[0]
        return self

    def __next__(self):
        if self.n is not None:
            current = self.n
            self.n = self.n.next
            return current.key, current.value

        self.b += 1

        if self.b == self.capacity:
            raise StopIteration

        self.n = self.buckets[self.b]
        return self.__next__()


if __name__ == '__main__':
    table = HashTable()

    for i in range(1000):
        table[i] = i + 1
        assert table[i] == i + 1
        assert table[chr(i)] is None

    assert len(table) == 1000

    for k, v in table:
        print(k, v)