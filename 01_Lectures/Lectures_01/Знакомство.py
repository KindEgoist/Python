# Переменные. 

# a = 123
# b = 1.23
# s = 'Privet Mir'
# print (f'{a} = {type(a)}, {b} = {type(b)}, {s} = {type(s)}')
# print (type(a))
# print (b)
# print (type(b))
# print (s)
# print (type(s))

# Списки (массивы).

# list = []
# list2 = [1, 2, 3]
# list3 = ['1', '2', '3', 'hello']
# list4 = [1, 2, 3, '1', '2', '3', 'hello', True]
# print(list, list2, list3, list4)

# Ввод и вывод

# print('Введите а: ') # будет строкой
# a = input()
# print('Введите b: ') # будет числом
# b = int (input())
# c = float (input('Введите с: '))
# print (f'{a} = {type(a)}, {b} = {type(b)}, {c} = {type(c)}') #вид формата записи
# print ("{} = {}, {} = {}, {} = {}".format(a, type(a), b, type(b), c, type(c))) #вид формата записи


# Арифметические опирации
# // деление в целых числах 12 // 8 = 1   423 // 10 = 42
# % остаток от делениея 12 % 8 = 4        423 % 10 = 3
# ** в степень

# a = 1.3
# b = 3
# c = a * b
# print (c)
# c = round (a * b, 3) # round сколько знаков оставить
# print (c)

#Логические опирации

# a = 1 > 4 #False
# b = 1 < 4 #True
# c = 1 < 4 and 5 > 2 #True
# d = 1 == 2 #False
# e = 1 != 2 #True
# f = 1 > 2 or 4 < 6 # True
# g = [1, 2, 3, 4] # False
# print (a, b, c, d, e, f, not 2 in g)

# list = [1, 2, 3, 4] #False
# is_odd = list = not list[0] % 2 # is_odd = list [0] % 2 == 0 вариант записи
# print (is_odd)

# Управляющая конструкция if, if - else, if - elif - else

# a = int (input('a = '))
# b = int (input('b = '))
# if a > b:
#     print ('a > b')
# elif a == b:
#     print ('a = b')
# else:
#     print ('b > a')

# Управляющая конструкция while

# original = 23
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
# else:
#     print ('Пожалуй')
#     print ('хватит')
# print (inverted)

# Управляющая конструкция for

# for i in 1, 2, 3, 4, 5:
#     print (i ** 2)

# list = [1, 2, 3, 4, 5]
# for i in list:
#     print (i ** 3)

# r = range (10) # range(10) от 0 до 9
# for i in r: # или for i in range (10)
#     print (i)

# for i in range (2, 10): # от 2 до 9
#     print (i)

# for i in range (1, 10, 2): # от 1 до 9 исключая 2
#     print (i)

# Строки

# text = 'съешь еще этих мягких'
# print (len(text)) #количество символов 21
# print ('еще' in text) # есть ли в тексте 'еще' True
# print (text.isdigit()) # являются ли числами False
# print (text.islower()) # нижний регистр True
# print (text.replace('еще', 'ЕЩЕ')) # замена 'еще' на 'ЕЩЕ'
# print (text[0]) # с
# print (text[1]) # ъ
# #print (text[len(text)]) #IndexError
# print (text[len(text)-1]) # х
# print (text[-5]) # я
# print (text[:]) # весь текст
# print (text[:2]) # съ # первых 2 символа
# print (text[10:]) # с конца 10 символов
# print (text[len(text)-2:]) # их
# print (text[2:9]) # ещь еще # срез с 2 элемента по 9
# print (text[6:-18]) # ХЗХЗХЗ
# print (text[0:len(text):6]) # сеик
# print (text[::6]) # сеик # шаг 6, каждый 6 элемент
# print (text[2:9]+text[-5]+text[:2]) # ешь ещеясъ

#help () # вызов справки
# например help (int)

# Список.
# range есть рендж
# list есть список

# ran = range (1, 6)
# print (range (1, 6))
# print (type(ran))
# numbers = list(ran)
# print (numbers)
# print (type(numbers))

# colors = ['red', 'green', 'blue']
# for e in colors:
#     print (e) # red, green, blue
# for e in colors:
#     print (e * 2) # redred, greengreen, blueblue
# colors.append('grey') # добавляет в конце списка Грей
# print (colors == ['red', 'green', 'blue', 'grey']) # Тру
# colors.remove('red') # удаляет ред
# print (colors)

# Функции

# def f(x):
#     if x == 1:
#         return 'Целое'
#     elif x == 2.3:
#         return 2.3
#     else:
#         return
# ary = 1 #2.3
# print (f(ary))
# print (type(f(ary)))

# n = int(input('Введите число: '))
# flag = True
# i = 2
# while flag:
#     if n % i == 0:
#         flag = False
#         print(i)
#     elif i > n // 2:
#         print (n)
#         flag = False
#     i += 1