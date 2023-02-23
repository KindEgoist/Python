# Чтение
with open('leas8.txt', 'r', encoding='utf-8') as file:
    # text = file.read() # прочитает весь текст
    text = file.read().split() #сделает список
    # for el in text:
    #     print(el) # по буквам
    print(text)
    # while True:
    #     line = file.readline()
    #     if not line:
    #         break
    #     # print(line)
    #     print(line.strip())

#Запись
# with open('leas8_2.txt', 'w', encoding='utf-8') as file:
#     some_list = ['привет', 'пока']
#     for word in some_list:
#         file.write(word + '\n')

# Подсчитать количество встречаемых букв
# with open('leas8_2.txt', 'r', encoding='utf-8') as file:
#     find_letter = input('Введите букву: ')
#     count = 0
#     for letter in file.read():
#         if letter == find_letter:
#             count += 1
#     print(count)
#
# with open('leas8_2.txt', 'r', encoding='utf-8') as file:
#     find_letter = input('Введите букву: ')
#     print(file.read().count(find_letter))

#Задайте список из N элементов, заполненных числами из промежутка (-N до N). Найдите произведение элементов на указанных
# позициях. Позиция хранится в файле file.txt в одной страке одно число.

# from random import randint
# n = int(input('Колличество элементов в списке: '))
# some_list = [randint(-n, n) for _ in range(n)]
# print(some_list)
#
# with open('file.txt', 'w', encoding='utf-8') as file:
#     for _ in range(randint(1, n)):
#         file.write(str(randint(0, n - 1)) + '\n')
#
# with open('file.txt', 'r', encoding='utf-8') as file:
#     mult = 1
#     for ind in file.read().splitlines():
#         mult *= some_list[int(ind)]
# print(mult)