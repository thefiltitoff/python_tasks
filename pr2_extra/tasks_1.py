import random
import sys
import os

#task 1 Преобразовать элементы списка s из строковой в числовую форму
print("1.Преобразовать элементы списка s из строковой в числовую форму")
def to_list(list):
    return [int(i) for i in list]

mass = ['1', '2', '3', '4']
print(mass)
print(to_list(mass))

#task
print("2.Подсчитать количество различных элементов в последовательности s.")
def count(list):
    return len(set(list))

s = ['2', '3', '3', '4', '5', True, 1, False]
print(count(s))

#task 3 Обратить последовательность s без использования функций.
print("3.Обратить последовательность s без использования функций.")
def reverse(lst):
    return lst[::-1]


s = ['1', '2', '3', '4', '5', True, 1, False]
print(reverse(s))

#task 4 Выдать список индексов, на которых найден элемент x в последовательности s.

print("4.Выдать список индексов, на которых найден элемент x в последовательности s.")
def index(lst, x):
    return [idx for idx, e in enumerate(lst) if e == x]

x = '6'
s = ['1', '3', '4', '6', '3', True, 1, '6']
print(index(s, x))

#task 5
#Сложить элементы списка s с четными индексами.
print("5.Сложить элементы списка s с четными индексами.")
def e_sum(lst):
    return sum(lst[::2])

s = [11, 100, 6, 3, 1, 5, 13]
print(e_sum(s))

#task 6 Найти строку максимальной длины в списке строк s.
print("6.Найти строку максимальной длины в списке строк s.")
def max_str(lst):
    return max(len(i) for i in lst)


s = ['qwe', 'qwerty', 'qw', 'qwerty12', 'qwe12345678', 'q']
this = 0
for i in range(len(s)):
    if len(s[i])>len(s[this]):
        this = i
print(s[this])

# сокращение символов
print("Cокращение символов")
def shorter():
    i = 0
    return 'mcwuoocdwhe'[i::3]

print(shorter())


#Напишите функцию generate_groups()



def generate_groups():
    list_groups = {'K': 25, 'B': 13, 'M': 2, 'H': 10}
    with open('groups.txt', 'w') as file:
        for k, v in list_groups.items():
            for n in range(1, v + 1):
                file.write('{}{}\n'.format(k, n))
generate_groups()

#zip and *
s1 = {2, 3, 1}
s2 = {'b', 'a', 'c'}

print(list(zip(s1, s2)))

def sum_num(*nums):
    s = 0
    for n in nums:
        s += n
    return s


print(sum_num(1, 2, 3, 5))
print(sum_num(4, 5, 6, 7, 8))

s = [1, 2, 3, 4, 5]
print(*s)

# transpose

def transpose(matrix):
    return list(list(i) for i in zip(*matrix))
mtrx1 = [[1, 2, 3],
      [4, 5, 6]]
mtrx2 = [[1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]]
print(transpose(mtrx1))
print(transpose(mtrx2))

text = [
    ['Коллеги,', 'В то же время,', 'Однако,', 'Тем не менее,', 'Следовательно,', 'Соответственно,', 'Вместе с тем,',
     'С другой стороны,'],
    ['парадигма цифровой экономики', 'контекст цифровой трансформации', 'диджитализация бизнес-процессов',
     'прагматичный подход к цифровым платформам', 'совокупность сквозных технологий',
     'программа прорывных исследований', 'ускорение блокчейн-транзакций', 'экспоненциальный рост Big Data'],
    ['открывает новые возможности для', 'выдвигает новые требования', 'несёт в себе риски', 'расширяет горизонты',
     'заставляет искать варианты', 'не оставляет шанса для', 'повышает вероятность', 'обостряет проблему'],
    ['дальнейшего углубления', 'бюджетного финансирования', 'синергетического эффекта',
     'компрометации конфиденциальных', 'универсальной коммодитизации', 'несанкционированной кастомизации',
     'нормативного регулирования', 'практического применения'],
    ['знаний и компетенций.', 'непроверенных гипотез.', 'волатильных активов.', 'опасных экспериментов.',
     'государственно-частных партнёрств.', 'цифровых следов граждан.', 'нежелательных последствий.',
     'внезапных открытий.']
]


def generate():
    return ' '.join(random.choice(i) for i in text)

for _ in range(20):
    print(generate())

#myprint

def my_print(*args, sep=" ", end="\n"):

    sys.stdout.write(sep.join(str(i) for i in args) + end)

print("Стандартная print():", "java", [1, 2], None, False, sep="\t->\t", end="%\n")
my_print("Саморучная:", "java", [1, 2], None, False, sep="\t->\t", end="%\n")


# именнованные аргументы
def only_name(**mass):
    for key, value in mass.items():
        print("{} is {}".format(key, value))


only_name(name='Титов Феликс', gender='a man')

#Напишите функцию generate_array
def generate_array(*dim):
    return [*dim]

arr = generate_array([1, 2], [3, 4], [5, 6])
print(arr)


import random

first_names=('Анатолий',' Аркадий','Артур', 'Валентин', 'Василий')
last_names=('Смирнов','Попов','Петров','Соколов','Михайлов')
sred = ('В.','Г.','Ш.','К.','Л.',)

group=" ".join(random.choice(first_names)+" "+random.choice(sred)+" "+random.choice(last_names) for _ in range(5))


print(group)


