"""
Использование встроенных функций
Напишите код, который выведет на экране все переменные объекта произвольного пользовательского класса.
Напишите код, который по имени метода, заданному строкой, вызовет этот метод в объекте некоторого пользовательского класса.
"""

import own_hash


def get_object_variables(obj):
    return [x for x in dir(obj) if not x.startswith('__')]

def invoke_object_method(obj, m):
    try:
        func = getattr(obj, m)
        return func()
    except AttributeError:
        print('Method do not found')


if __name__ == '__main__':
    table = HashTable()
    print(get_object_variables(table))
    print(invoke_object_method(table, '__len__'))