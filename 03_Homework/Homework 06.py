# Задача 1: Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно
# ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
# Ввод: 7 2 5
# Вывод: 7 9 11 13 15

# a1 = int(input('Первый элемент: '))
# d = int(input('Разность элементов: '))
# n = int(input('Количество элементов: '))
#
# lst = []
# for i in range(n):
#     if i == 0:
#         lst.append(a1)
#     else:
#         lst.append(lst[i - 1] + d)
# print(lst)

# Задача 2: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного максимума)
# Ввод: [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]

# from random import randint
# lst = [randint(-10, 10) for i in range(int(input('Длина списка: ')))]
# mini = int(input('MIN значение: '))
# maxi = int(input('MAX значение: '))
# print(lst)
# print(list(i for i in range(len(lst)) if mini <= lst[i] <= maxi))