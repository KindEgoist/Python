# Задача 1: Дан список чисел. Определите, сколько в нем встречается различных чисел.

# lst = [10, 20, 5, 7, 7, 9]
# lst = set(lst)
# print(len(lst))

# Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность (сдвиг - циклический)
# на K элементов вправо, K – положительное число.

#???ПОД ВОПРОСОМ???
# lst = [10, 20, 5, 7, 7, 9]
# k = 3
# lst_result = list()
# for i in range(k):
#     lst_result.append(lst[len(lst) - 1 - i])
#     print(lst_result)
# print()
# for i in range(len(lst) - k):
#     lst_result.append(lst[i])
#     print(lst_result)
# print(lst_result)

# Задача 2: Напишите программу для печати всех уникальных значений в словаре. \
# list_1 = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
#               {"VII": "S005 "}, {" V ":" S009 "}, {" VIII ":"S007 "}]
# set_1 = set()
# for i in list_1:
#     for j in i:
#         set_1.add(i[j])
# print(set_1)


#
# Задача 3: Дан массив, состоящий из целых чисел. Напишите программу, которая подсчитает количество элементов
# массива, больших предыдущего (элемента с предыдущим номером). list_1 = [0, -1, 5, 2, 3]

list_1 = [0, -1, 5, 2, 3]
n = 0
for i in range(1, len(list_1)):
    if list_1[i] > list_1[i - 1]:
        n += 1
print(n)