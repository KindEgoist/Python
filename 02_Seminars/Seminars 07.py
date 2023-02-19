#Примеры:
# 1) map

# перевести каждый элемент в строку
# обычный вариант

# lst = [1, 2, 3, 4, 5]
# for i in range(len(lst)):
#     lst[i] = str(lst[i])
# print(lst)

# вариант map
# lst = [1, 2, 3, 4, 5]
# lst = list(map(str, lst)) # первый аргумент любая функция, второй любой интерьируемый объект c которым мы хотим что-то сделать
# print(lst)

#2) filter

# оставить только четные элементы из списка
# lst = [1, 2, 3, 4, 5, 6]
# def even(x):
#     return x % 2 == 0
# lst = list(filter(even, lst)) # первый аргумент любая функция, второй любой интерьируемый объект который мы хотим отфильтровать
# print(lst)

# 3) lambda
# lst = [1, 2, 3, 4, 5, 6, 8]
# lst = list(filter(lambda x: x % 2 == 0, lst)) # пример из фильтра с добавлением lambda
# print(lst)

# 4) enumerate работа с индексами и элементами одновременно
# lst = [10, 20, 30, 40]
# print(list(enumerate(lst)))
# for i, v in enumerate(lst):
#     print(i, v)
#     if 20 <= v < 35:
#         print(i)

# 5) zip сшитие коллекций
# one_lst = ['apple', 'orange', 'grape']
# two_lst = ['яблоко', 'апельсин', 'виноград']
# for eng, ru in zip(one_lst, two_lst):
#     print(eng, ru)

# У вас есть код, который вы не можете менять (так часто бывает, когда код в глубине программы используется множество
# раз и вы не хотите ничего сломать):
# transformation = <???>
# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
# transormed_values = list(map(transformation, values))
# Единственный способ вашего взаимодействия с этим кодом - посредством задания функции transformation.
# Однако вы поняли, что для вашей текущей задачи вам не нужно никак преобразовывать список значений, а нужно получить
# его как есть.
# Напишите такое лямбда-выражение transformation, чтобы transformed_values получился
# копией values.
# Ввод:
# values = [1, 23, 42, ‘asdfg’]
# transformed_values = list(map(trasformation, values))
# if values == transformed_values:
# print(‘ok’)
# else:
# print(‘fail’)
# Вывод: ok
# transformation = lambda x: x
# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
# transformation_values = list(map(transformation, values))
# print(transformation_values)
# if values == transformation_values:
#     print('ok')
# else:
#     print('fail')


# Планеты вращаются вокруг звезд по эллиптическим орбитам. Назовем самой далекой планетой ту, орбита которой имеет
# самую большую площадь. Напишите функцию find_farthest_orbit(list_of_orbits), которая среди списка орбит
# планет найдет ту, по которой вращается самая далекая планета. Круговые орбиты не учитывайте: вы знаете, что у
# вашей звезды таких планет нет, зато искусственные спутники были были запущены на круговые орбиты. Результатом
# функции должен быть кортеж, содержащий длины полуосей эллипса орбиты самой далекой планеты. Каждая орбита
# представляет из себя кортеж из пары чисел - полуосей ее эллипса. Площадь эллипса вычисляется по формуле S = pi*a*b,
# где a и b - длины полуосей эллипса. При решении задачи используйте списочные выражения. Подсказка: проще всего
# будет найти эллипс в два шага: сначала вычислить самую большую площадь эллипса, а затем найти и сам эллипс,
# имеющий такую площадь. Гарантируется, что самая далекая планета ровно одна
# Ввод:
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(*find_farthest_orbit(orbits))
# Вывод:
# 2.5 10
import math
# S = pi*a*b,
# # где a и b - длины полуосей эллипса

# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# new = list(filter(lambda x: x[0] != x[1], orbits))
# new_max = max(map(lambda x: x[0] * x[1] * math.pi, new))
# print(list(filter(lambda x: x[0] * x[1] * math.pi == new_max, new)))

# Дан массив с числами, и целевое значение. Нужно проверить найдутся ли в массиве два числаб чья сумма равна целевому
#значению.
#
# summa = 182
# summa_list = [98, 19, 48, 24, 12, 84]
#
# for e in summa_list:
#     if summa - e in summa_list:
#         print('yes')
#         break
# else:
#     print('no')
#
# summa_set = set(summa_list)
# for e in summa_set:
#     if summa - e in summa_set:
#         print('yes')
#         break
# else:
#     print('no')

# Напишите функцию same_by(characteristic, objects), которая проверяет, все ли объекты имеют одинаковое значение
# некоторой характеристики, и возвращают True, если это так. Если значение характеристики для разных объектов
# отличается - то False. Для пустого набора объектов, функция должна возвращать True. Аргумент characteristic - это
# функция, которая принимает объект и вычисляет его характеристику.
# Ввод:
# values = [0, 2, 10, 6]
# if same_by(lambda x: x % 2, values):
# print(‘same’)
# else:
# print(‘different’)
# Вывод:same

def same_by(characteristic, objects):
    if len(objects) == 0:
        return True
    for i in range(len(objects)):
        if characteristic(objects[i]) != characteristic(objects[0]):
            return False
    return True

values = [0, 2, 10, 6]
if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')