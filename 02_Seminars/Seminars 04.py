# Задача 1. Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к символам с помощью постфикса формата _n.

# lst = input('Введите через пробел строку: ').split()
# print(lst)
# lst = 'a a a b c a a d c d d'.split()
# print(lst)
# lst = ['a', 'a', 'a', 'b', 'c', 'a', 'a', 'd', 'c', 'd', 'd']
# print(lst)
# dic = {}
# lst_new = []
# for e in lst:
#     dic[e] = dic.get(e, 0) + 1 #    берем елемент из списка ввиде ключа, если в списке повторяется еслемент то к
#     # созданному ключу добавляем значение +1, если такого елемента нет то создается ключь с значением 1
#     if dic.get(e) > 1:
#         lst_new.append(f'{e}_{str(dic.get(e))}')
#     else:
#         lst_new.append(e)
# print(dic)
# print(lst_new)
# print(' '.join(lst_new))

# lst = 'a a a b c a a d c d d'.split()
# for i in range(len(lst)):
#     count = 1
#     for j in range(i + 1, len(lst)):
#         if lst[i] == lst[j]:
#             count += 1
#             lst[j] = f'{lst[j]}_{count}'
# print(' '.join(lst))

# Задача 2.Пользователь вводит текст(строка). Словом считается последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом пробелов. Определите, сколько различных слов
# содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells
# Output: 13
# str = set("Input: She sells sea shells on the sea shore The   shells that she sells are sea shells I'm sure.So if she sells sea  shells on the sea shore I'm sure that the shells are sea shore shells".split())
# print(len(str))

# Задача 3. Дана последовательность чисел. ПОлучить список уникальных элементов заданной последовательноти
# Пример [1, 2, 3, 5, 1, 5, 10] - > [2, 3, 10]

# lst = [1, 2, 3, 5, 1, 5, 10]
# dic = {}
# lst_new = []
# for e in lst:
#      dic[e] = dic.get(e, 0) + 1
# print(dic)
# for i in dic:
#     if dic.get(i) == 1:
#         lst_new.append(i)
# print(lst_new)

lst = [1, 2, 3, 5, 1, 5, 10]
print(lst)
lst_new = []
for e in lst:
    if lst.count(e) == 1:
        lst_new.append(e)
print(lst_new)
print([e for e in lst if lst.count(e) == 1])