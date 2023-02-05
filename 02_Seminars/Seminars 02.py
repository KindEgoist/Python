# Задача 1.
# По данному целому неотрицательному n вычислите значение n!. N! = 1 * 2 * 3 * … * N (произведение всех чисел от 1 до N) 0! = 1 Решить задачу используя цикл while

# n = int(input("Введите число: "))
# factorial = 1
# if n > 1:
#     while n > 1:
#         factorial *= n
#         n -= 1
#     print(f'Факториал равен {factorial}')
# else:
#     print('Факториал равен 1')

# Задача 2.
# Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является, то есть выведите такое число n, что φ(n)=A. 
# Если А не является числом Фибоначчи, выведите число -1

# a = int(input('Введите число: '))
# count = 1
# f1 = 1
# f2 = 0
# tmp = 0
# if a == f2:
#     print(1)
# elif a == f1:
#     print(1)
# else:
#     while a > tmp:
#         tmp = f1 + f2
#         f2 = f1
#         f1 = tmp
#         count += 1
#     if a == tmp:
#         print(count + 1)
#     else:
#         print(-1)


# Задача 3.
# Уставшие от необычно теплой зимы, жители решили узнать, действительно ли это самая длинная оттепель за всю историю наблюдений за погодой. 
# Они обратились к синоптикам, а те, в свою очередь, занялись исследованиями статистики за прошлые годы. Их интересует, сколько дней длилась самая длинная 
# оттепель. Оттепелью они называют период, в который среднесуточная температура ежедневно превышала 0 градусов Цельсия. Напишите программу, помогающую 
# синоптикам в работе.

# Пользователь вводит число N – общее количество рассматриваемых дней (1 ≤ N ≤ 100). В следующих строках располагается N целых чисел.

# Каждое число – среднесуточная температура в соответствующий день. Температуры – целые числа и лежат в диапазоне от –50 до 50

# max_count = 0
# count = 0
# n = int(input('Введите количество дней: ')) # количество дней
# for _ in range(n): # запрос ввода температуры столько раз сколько дней
#     temp = int(input('Введите температуру: '))
#     if temp > 0:
#         count += 1
#     else:
#         if count > max_count:
#             max_count = count
#         count = 0
# if max_count == 0 and count != 0:
#     print(count)
# else:
#     print(max_count)

from random import randint

max_count = tmp_count = 0
n = int(input('Введите количество дней: '))
lst = list(randint(-50, 50) for i in range(n))
print(lst)
for e in lst:
    if e > 0:
        tmp_count += 1
        if max_count < tmp_count:
            max_count = tmp_count
    else:
        tmp_count = 0

print(max_count)

# Задача 4.
#  Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя, а другой для тещи. Понятно, что для себя нужно выбрать арбуз потяжелей, 
#  а для тещи полегче. Но вот незадача: арбузов слишком много и он не знает как же выбрать самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество арбузов. Вторая строка содержит N чисел, записанных на новой строчке каждое. Здесь каждое число – 
# это масса соответствующего арбуза. Все числа натуральные и не превышают 30000.

from random import randint
n = int(input('Введите количество арбузов: '))
lst = list(randint(10000, 30000) for i in range(n))
print(lst)
max_sebe = 0
min_teshi = lst[0]
for e in lst:
    if e > max_sebe:
        max_sebe = e
for e in lst:
    if e < min_teshi:
        min_teshi = e
print (f'Себе = {max_sebe}, Тещи = {min_teshi}')