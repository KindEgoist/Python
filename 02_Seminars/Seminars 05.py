# Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ..., где
# a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1). Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 21

# 0 1 2 3 4 5 6 7  8  9
# 0 1 1 2 3 5 8 13 21 34

# def fib(num):
#     if num == 0:
#         return  0
#     elif num == 1:
#         return  1
#     else:
#        return fib(num - 1) + fib(num - 2)
#
# n = int(input('Введите число: '))
#
# print(f'Список: {list(fib(i) for i in range(n))}')
# print(f'Число фибоначи: {fib(n)} под номером {n}')


# Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные.
# Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1
# 2 3 4 2 3 4 3 4
# 2 3 2 2 3 2 3 2
#
# 5 5 5 5 5 5 5 5
# 5 5 5 5 5 5 5 5
#
# 4 5 4 5 5 5 5 4
# 4 4 4 4 4 4 4 4

import time

# lst = input('Введите оценки через пробел:').split()
# print(lst)
#
# start = time.perf_counter()
# maximum = max(lst)
# minimum = min(lst)
# end = time.perf_counter()
# print(end - start)
#
# start = time.perf_counter()
# maximum = lst[0]
# minimum = lst[0]
# for e in lst:
#     if e < minimum:
#         minimum = e
#     elif e > maximum:
#         maximum = e
# end = time.perf_counter()
# print(end - start)
#
# for i in range(len(lst)):
#     if lst[i] == maximum:
#         lst[i] = minimum
# print(lst)

# Напишите функцию, которая принимает одно число и проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes
# start = time.perf_counter()
# def pro(n):
#     lst = list(i for i in range(1, n + 1) if n % i == 0)
#     if len(lst) == 2:
#         print(f'Число {n} простое')
#     else:
#         print(f'Число {n} не простое')
#
# pro(int(input('Введите число: ')))
# end = time.perf_counter()
# print(end - start)
#
# start = time.perf_counter()
# def pro2(n):
#     for i in range(2, n // 2 + 1):
#         if n % i == 0:
#             print('Число не простое')
#             break
#     else:
#         print('Число простое')
# pro2(int(input('Введите число: ')))
# end = time.perf_counter()
# print(end - start)