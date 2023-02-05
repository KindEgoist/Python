#Запись и перезапись

# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'a') #переменная data. open()-открыть. файл file.txt и модификатор а
# data.writelines(colors) #производим запись .разделителей не будет
# data.close #разрыв соединения


# data = open('file.txt', 'a') 
# data.write('\nLINE 2\n')
# data.write('LINE 3\n')
# data.close

# with open('file.txt', 'w') as data: # создает и принимать в переменную data (as data) выше стояющию конструкцию open('file.txt', 'w')
#     data.write('\nLine 2\n')
#     data.write('Line 3\n') # в конце автоматически сделает разрыв соединения 

#Чтение файла

# path = 'file.txt' #путь к файлу
# data = open(path, 'r') # чтение
# for line in data: # c помощью цикла пробегаем по файлу и считываем все строки
#     print(line)
# data.close()

# Импорт

# import funF as h #импортируем файл как модуль из тойжу папки где находимся. переменовали funF в h. В дальнейшем обращаемся вместо funF по h
# print(h.f(1))

# Работа с функциями и ее аргументами

# def new_string(symbol, count = 3):
#     return symbol * count
# print(new_string('!', 5)) # !!!!! 
# print(new_string('!')) # !!!
# print(new_string(4)) # 12

# def concatanatio(*params): # *- позволяет добавить аргументы
#     res: str = "" # присваеваем к переменной res тип строки
#     for item in params:
#         res += item
#     return res

# print(concatanatio('a', 's', 'd', 'w')) # asdw
# print(concatanatio('a', '1')) #a1
# #print(concatanatio(1, 2, 3, 4))

# Рекурсия

# def fib(n):
#     if n in [1, 2]:
#         return 1
#     else:
#         return fib(n - 1) + fib(n - 2)
# list = []
# for e in range(1, 10):
#     list.append(fib(e))
# print(list)

# Кортежи - это неизменяемый "список"

# a = (3, 1, 41, 4)
# print(a) # 3, 1, 41, 4 обращаться можно как со списком
# print(a[-2]) #41
# a[0] = 12# ошибка, нельзя изменить

# t = tuple (['red', 'green', 'blue'])
# red, green, blue = t
# print ('r:{} g:{} b:{}'.format(red, green, blue)) 

# Словари - Неупорядочнные коллекции произвольных объектов с доступом по ключу

# объявление словаря. \ позволяет писать не в одну строчку данные а так как ниже. up и т.д. выступают в виде ключей
# dictionary = {}
# dictionary = \
#     {
#         'up': '↑',
#         'left': '←',
#         'down': '↓',
#         'rught': '→'
#     }
# print(dictionary) #{'up': '↑', 'left': '←', 'down': '↓', 'rught': '→'
# print(dictionary['left']) # ←

# for k in dictionary.keys(): #перебор по ключам
#     print(k)
# for k in dictionary.values(): #перебор по значениям
#     print(k)

# Множества

# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}
# c = a.copy() # копируем а в переменную с с = {1, 2, 3, 5, 8}
# u = a.union(b) # объединяет a с b u = {1, 2, 3, 5, 8, 13, 21}  
# i = a.intersection(b) # пересечение {8, 2, 5}
# dl = a.difference(b) #{1, 3}
# dr = b.difference(a) #{13, 21}

# q = a \
#     .union(b) \
#     .difference(a.intersection(b)) #{1, 21, 3, 13}
# print(a)
# print(b)
# print(c)
# print(u)
# print(i)
# print(dl)
# print(dr)
# print(q)

# s = frozenset(a) # не изменяемые множества

# Списки

# lst = [1, 2, 4, 9]
# print(lst) #[1, 2, 4, 9]
# print(*lst) #1 2 4 9
# lst.insert(2, 11) # добавление элемента на определенную позицию
# print(lst)
#
# # Срезы тоже работают в списках

# Кортедж

# kort = (1, 2, 5, 8, )
# print(type(kort)) #tuble
# print(kort)
# a, b, c, e = kort
# print(a, b, c, e)


