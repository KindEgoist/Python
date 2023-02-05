# Конвертор миль в км
# def convert(mili):
#     return mili * 1.609

# mili = float(input('Введите число миль: '))
# km = convert(mili)
# print(f'{mili} милей = {km} километров')
#---------------------------------------------
#Площадь примоугольника по двум сторанам
# def rectangle_area (a, b):
#     return a * b

# length = int(input('Введите число дилины: '))
# width = int(input('Введите число ширина: '))
# s = rectangle_area(length, width)
# print (f'Площадь прямоугольника = {s}')
#---------------------------------------------
#Чет не чет
# def even_or_not_even(num):
#     if num % 2 == 0:
#         return 'Четное'
#     else:
#         return 'Не чет'
# ever = int(input('Введите число: '))
# result = even_or_not_even(ever)
# print(result)
#-----------------------
# Если n > 20 то вернуть 0. Если n <= 20 то пробежаться от 1 до n, возвести каждое четное число в степерь k и вернуть сумму этих чисел
# def function (n, k):
#     if n > 20:
#         return 0
#     else:
#         sum = 0
#         for i in range(2, n + 1):
#             if i % 2 == 0:
#                 res = i ** k
#                 sum += res
#                 print(f'{i} - {res} - {sum}')
#         return sum

# n = int(input('Введите n: '))
# k = int(input('Введите k: '))
# result = function(n, k)
# print (result)
#-----------------------------
# list = [3, 5, 7, 9]

# print('по индексу к элементу')
# for i in range(len(list)):
#     print(f'{i} = {list[i]}')

# print ('Сразу по элементам списка')
# for i in list:
#     print(i)
#-------------------------------
#Сумма отрицательных элементов(идти только по отрицательным)
# list = [-5, -10, -13, -15, -18]
# list = [7, 5, 4, 4, 3, 2, 1, -5, -10, -13, -15, -18]
# sum = 0
# i = len(list) -1 
# while list[i] < 0 and i >= 0:
#     sum += list[i]
#     i -= 1
# print(sum)

# sum = 0
# for i in range(len(list) - 1, -1, -1): # движение по листу с конца к началу
#     if list[i] > 0:
#         break
#     sum += list[i]
# print(sum)
#-----------------------------------
#     
# list = ["apple", "banana", "computer", "music", "stop", "these", "words", "will", "not", "be", "printed"]

# for i in list:
#     if i == "stop":
#         break
#     print(i)

# for i in range(len(list)):
#     if list[i] == "stop":
#         break
#     print(list[i])

# i = 0
# while list[i] != "stop":
#     print(list[i])
#     i += 1
#---------------------------------
# Словари
# # объявление словаря. Пример: dictionary = {}
# d = {"Alex": 25, "Petr": 37} # Ключ : значение
# print(d) # Вывели весь словарь
# print(len(d)) #Длина словаря = 2( две пары)
# d["Kate"] = 18 # Добавит в конец словаря "Kate" : 18
# print(d)
# print(d["Petr"]) # отбращаемся в словаре по ключу и получаем значение
# d["Kate"] = 24 # изменили значение ключа
# print(d)
# d[10] = 20
# del(d["Alex"]) #удаление
# print(d)
# for k, v in d.items(): #проходим по словарю d.keys() по ключам d.values() по значениеям
#     print(k) # отдельно выводим ключ
#     print(v) #отдельно выводим значение
#     print(f'Ключ = {k} и его значение = {v}')
#------------------------------
# Из строки сделать словарь. Где ключь слово, а значение цифры

# list = ['first', 1, 2, 3, 'second', 10, 20, 'third', 15, 70, 'fourth', -50]
# dictionary = {}
# key = None # переменная которая не содержит нечего
# for e in list: # идем по элементам списка
#     if type(e) == str: # если элемент строка, то
#         dictionary[e] = [] # этот элемент добавляем в словарь с пустым значением
#         key = e # в временную переменную записываем элемент для дальнейшего обращения
#     else:
#         dictionary[key].append(e) # добавляем значение в ключ 
    
# print(dictionary)
#--------------------------
# Создать словарь где ключи будут слова а их значение сколько раз они поподаются в тесте
# text = 'привет пока как дела привет привет арбуз велосипед стол как слон арбуз да привет'

#Вариант мой
# list = text.split()
# dictionary = {}
# key = None
# for e in list:
#     count = 0
#     dictionary[e] = []
#     key = e
#     for e2 in list:
#         if key == e2:
#             count += 1
#     dictionary[key].append(count)
# print (dictionary)

#Вариант 2
# dictionary = {} # создаем словарь
# for e in text.split(): # бежим по тексту со сплитом
#     if e in dictionary: # 2) если слово текущие есть то
#         dictionary[e] = dictionary[e] + 1 # к этому слову(ключу) добавляем значение +1
#     else:
#         dictionary[e] = 1 # 1)  если такого слова нет в словаре то его создаем в виде ключа с параметром 1
# print(dictionary)

# Вариант 3 через функцию get
# dictionary = {} 
# for e in text.split():
#     dictionary[e] = dictionary.get(e, 0) + 1
# print(dictionary)
#----------------------
# Многомерные списки или многомерные массивы
# Создать многомерный список n на m. Значение все нули

# def create_list (m, n): #создание многомерного списка
#     list = []
#     for i in range(m):
#         temp_list = []
#         for j in range(n):
#             temp_list.append(0)
#         list.append(temp_list)
#     return list

# def print_list (list): # функция печати многомерного списка
#     for s in range(len(list)):
#         for e in range(len(list[s])):
#             print(list[s][e], end= ' ')
#         print()

# m = int(input('M= : '))
# n = int(input('N= : '))
# list = create_list(m, n)
# print_list(list)
#---------------------
#Зеркальное отоброжение двухмерного списка

# def create_list (size):
#     list = []
#     count = 10
#     for i in range(size):
#         temp_list = []
#         for j in range(size):
#             temp_list.append(count)
#             count += 1
#         list.append(temp_list)
#     return list

# def print_list(list):
#     for i in range(len(list)):
#         for j in range(len(list[i])):
#             print(list[i][j], end= ' ')
#         print()

# def revers_list(list):
#     for i in range(len(list)):
#         for j in range(len(list) // 2): # // цело численное деление вместо for j in range(int(len(list) / 2))
#             list[i][j], list[i][-1 - j] = list[i][-1 - j], list[i][j]
#     return list


# size = int(input('Размер массива: '))
# list = create_list(size)
# print_list(list)
# print('Реверс массива:')
# list2 = revers_list(list)
# print_list(list2)
#------------------------------------
#Генераторы списков(List comprehension)

# list = [1, 2, 3, 4, 5]

# list2 = []
# for num in list:
#     list2.append(num * 2)
# print(list2)
# # сокращенная версия записи 
# list3 = [num * 2 for num in list]
# print(list3)
# # еще пример
# range = [num * 3 for num in range(1, 6)]
# print(range)
# еще пример

# list = [1, 10, 12, 4, 3, 20, 55]
# list_filter = []
# for num in list:
#     if num < 10:
#         list_filter.append(num)
# print(list_filter)

# list_filter2 = [num for num in list if num < 10]
# print(list_filter2)

# list_filter3 = [num ** 2 for num in list if num < 10]
# print(list_filter3)

# list = ['hello', 'hey', 'goodbay', 'guitar', 'piano']
# list_filter = [i for i in list if len(i) < 6]
# print(list_filter)
#-------------------------------
#Результат: [20, 16, 12, 8, 4]
# от 10 до 2. Идем по интервалу от большого к меньшему, берем только четные числа.
# каждое четное чилос мы умнажаем на 2

# list = [i*2 for i in range(10, 1, -1) if i % 2 == 0]
# print(list)
#---------------------
# list = ['hello', 'hey', 'goodbay', 'guitar', 'piano'] если длина больше 5 добавить точку в конце

# list = ['hello', 'hey', 'goodbay', 'guitar', 'piano']
# list_filter = [i + '.' for i in list if len(i) > 5]
# print (list_filter)
#-------------------------
# Множество SET

# set1 = set() # объявление пустого множества. set = {} было бы объявление словаря а не множества
# print(set1)

# set2 = set([1, 10, 5, 'hello']) # 1 способ создание множества
# print(set2)

# set3 = {20, 16, 'hey', 'goodbay', 'guitar'} # 2 способ создание множества
# print(set3)

# set4 = set()
# set4.add(1) # add() добовляет элемент в множество
# set4.add(2)
# set4.add('hello')
# set4.add(10)
# set4.add(2)
# print(set4) #множество хванится не попорядку(как добавляли) и все значение разные, не должно быть повторяющихся элементов

# for el in set4: #вывод всех элементов по очередно в множестве
#     print(el)

# set5 = set() # из списка перекинули элементы в множества, при этом убрали повторяющиеся элементы
# list1 = [1, 2, 1, 1, 5, 'hey', 'hey', 'world']
# # for el in list1:
# #     set5.add(el)
# # print (set5)

# set5 = set(list1) # другой вариант написанного выше без фор. Передали в виде аргумента и получили результат
# print(set5)
# list1 = list(set5) # в лист в качестве аргумента передаем множество
# print(list1)

# set6 = {'hey', 'world',1, 5, 10}
# print(5 in set6) #True ищет указанное значение с помощью (in) в множестве\словаре\списке и т.д.
# print('hey' in set6) #True
# print(2 in set6) #False
# print(15 not in set6) #True
#--------------------------
# Из списка выделить уникальные элементы и получить их сумму
# list1 = [1, 1, 2, 5, 10, 10, 10]
# sum1 = 0
# set1 = set(list1)
# for el in set1:
#     sum1 += el
# print(sum1)
# print(sum(set(list1)))# решение одной строкой. Используем функцию sum() в нее в виде аргумента помещаем функцию set()
# #у которой в качестве аргумента наш список
#----------------------
#Тру если все элементы из списка содержится в множестве. Фолс если нет хоть одного элементы в списки



# def fine (set1, list1):
#     if len(set1) < len(list1):
#         return False
#     for el in list1:
#         if  el not in set1:
#             return False
#     return True
    
# set1 = set([1, 5, 10, 4, 'helloy'])
# list1 = [1, 4, 10, 'helloy']
# x = fine(set1, list1)
# print (x)
#-----------------------
# Объектно орентированное программирование(ООП).

# class Person: #Классы всегда называются с большой буквы
#     def print_info(self,n):
#         for i in range(n):
#             print(f'Name: {self.name}, Surname: {self.surname}, Place of birth: {self.place_of_birth}')
#     def get_age(self, current_year):
#         print(f'Age: {current_year - self.year_of_birth}')


# p1 = Person() #создание пустого классы в переменной
# p1.name = 'Elon'
# p1.surname = 'Musk'
# p1.place_of_birth = 'ЮАР'
# p1.year_of_birth = 1971

# p2 = Person() 
# p2.name = 'Sergei'
# p2.surname = 'Korolev'
# p2.place_of_birth = 'Российская Империя'
# p2.year_of_birth = 1907

# p3 = Person() 
# p3.name = 'Albert'
# p3.suname = 'Einstein'
# p3.year_of_birth = 1879
# # cсделана ошибка в suname и не назначели поле p2.place_of_birth

# # print(f'Name: {p1.name}, Surname: {p1.surname}, Place of birth: {p1.place_of_birth}')
# # print(f'Name: {p2.name}, Surname: {p2.surname}, Place of birth: {p2.place_of_birth}')
# p1.print_info(2) #вызов функции print_info где аргумент будет выступать параметр p1 вместо аргумента в self 
# p2.print_info(1)

# #Person.print_info(p1,3) # Обращаемся к классу Person и его функции print_info c аргументом p1. Вместо p1.print_info()
# p1.get_age(2022)
# p2.get_age(2022)

# class Person: 
#     def __init__(self, name, surname, place_of_birth, year_of_birth): # функция конструктора. Вместо повторяющегося кода
#         self.name = name
#         self.surname = surname
#         self.place_of_birth = place_of_birth
#         self.year_of_birth = year_of_birth
#     def print_info(self,n):
#         for i in range(n):
#             print(f'Name: {self.name}, Surname: {self.surname}, Place of birth: {self.place_of_birth}')
#     def get_age(self, current_year):
#         print(f'Age: {current_year - self.year_of_birth}')


# p1 = Person('Elon', 'Musk', 'ЮАР', 1971)
# p2 = Person('Sergei', 'Korolev', 'Российская Империя', 1907)
# p3 = Person('Albert', 'Einstein', 'Германия', 1879)

# p1.print_info(1)
# p2.print_info(1)
# p3.print_info(1)

# class Circle:
#     PI = 3.14

#     def __init__(self, radius):
#         self.radius = radius
#     def get_perimeter(self):
#         return self.radius * 2 * self.PI
#     def get_area(self):
#         return Circle.PI * self.radius ** 2

# c1 = Circle(3)
# print(c1.get_perimeter())
# print(c1.get_area())
# print()
# c2 = Circle(7)
# print(c2.get_perimeter())
# print(c2.get_area())
#-------------------------------

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         print('Person created')
#     def say_hello(self):
#         print(f'{self.name} says hello!')

# class Student(Person):
#     def __init__(self, name, age, average_grade):
#         #Person.__init__(self, name, age)
#         super().__init__(name, age)
#         self.average_grade = average_grade
#         print('Student created')
#     def study(self):
#         print(f'{self.name} studies')
#     def say_hello(self):
#         super().say_hello()
#         print(f'Student with name {self.name} says hello!')

# class Teacher(Person):
#     def teach(self):
#         print(f'{self.name} teaches')

# # s1 = Student('Mike', 18, 4.5)
# # #t1 = Teacher('Katy', 45)
# # s1.say_hello()
# # #t1.say_hello()
# # s1.study()
# # #t1.teach()

# def introduce(person):
#     print('Now, a person will say hello')
#     person.say_hello()
# people_arr = [Student('Tom', 18, 3.5), Teacher('Katy', 35), Student('Bob', 26, 4.8)]
# for person in people_arr:
#     introduce(person)
#-------------------------------------------
# class Animal:
#     def __init__(self, name):
#         self.name = name
#     def eat(self):
#         print(f'{self.name} is eating')
# class Dog(Animal):
#     def __init__(self, name, breed):
#         super().__init__(name)
#         self.breed = breed
#     def bark(self):
#         print(f'Dog name {self.name} is barking')
# class Cat(Animal):
#     def meow(self):
#         print(f'{self.name} says Meow')
# class Frog(Animal):
#     def eat(self):
#         print(f'Frog with {self.name} is eating')

# d = Dog('Druzhok', 'Terrier')
# c = Cat('Barsik')
# f = Frog('Kwakwa')

# d.bark()
# d.eat()
# d.breed

# c.meow()
# c.eat()
# f.eat()
#-------------------------------------------
# a = 45
# b = 5
# def f():
#     global a # параметр global подтягивает значение глобальной переменной
#     a = a + 2
#     print(a)
# f()
# #----------------------
# list.append() # метод добавления в конец списка элемента.  В скобках какой элемент добавить
# list.pop() # удаляет последний элемент в списки. В качестве аргумента номер индекса который надо удалить.
# list.index() # метод показывающий номер индекса элемента. В скопках задается элемент
# len(list) # длина списка
# list.sort() # метод сортировки списка. Чтоб сделать сортировку наоборот в скобках указываем reverse = True
#------------------------
#текст заключенный в тройные ковычки может содержать хоть сколько строк

# print("""привет
# мир
# мир
# привет""")
# print('привет\nпривет') #перенос на новую строку /n
# print('привет\tпривет') #разделитель в одну табудяцию ./t
# print('"текст в кавычках"')
# print("текст \"в\" кавычках")

# text = 'Привет'
# print(text[0:3]) # : срез. в данном случае указали от 0 индекса до 3(не включает). Результат При
# print(text.upper()) # метод upper() делает все символы за главными
# print(text.lower()) # метод lower() делает все символы маленькими
# text2 = 'привет'
# print(text.capitalize()) # метод capitalize() делает первый символ заглавным
# text3 = 'привет мир куда идешь'
# print(text3.split()) # метод split() делает список где разделитель(по умолчанию) является пробел между словами. Если другой разделитель то он указывается в аргументе сплита
# spisok = ['a', 'b', 'c']
# print(','.join(spisok)) # метод join() создает строку где разделитель указывается перд ним. В данном случае разделитель будет запятая
# text4 = '         vsdsdgfs gsdg g sssd      '
# print(text4.strip()) # метод strip() удалит все пробелы в начале и в конце
# print(text4.lstrip()) # метод lstrip() удалит все пробелы в начале
# print(text4.rstrip()) # метод rstrip() удалит все пробелы в конце
# text5 = 'lololololololol'
# print(text5.replace('l', 'O')) # метод replace() заменит один символ на другой. Аргументы: первый какой символ, второй на какой заменить
# for i in text3:
#     print(i)
#-----------------------------------
# Модули
# import math # импорт модуля 
# print(math.factorial(10)) #изпользование в модули функцию факториал
# import math as m # вместо того чтоб не писать math дали ему имя m(можно любое)
# print(m.factorial(10))
# from math import factorial # импорт только одной функции из модуля
# print(factorial(10))
# from math import factorial as fac
# print(fac(10))
#------------------------
# Классы и объекты

# class House(): #класс
#     #описание дома
#     def __init__(self, street, number):
#         self.street = street
#         self.number = number
#         self.age = 0

#     def build(self):
#         # строит дом
#         print('Дом на улице ' + self.street + ' под номером ' + str(self.number) + ' построен.')

#     def age_of_house(self, year):
#         #возраст дома
#         self.age += year

# class ProspectHouse(House):
#     #дома на проспекте
#     def __init__(self, prospect, number):
#         super().__init__(self, number)
#         self.prospect = prospect

# # House1 = House('Московская', 20) #объекты
# # House2 = House('Московская', 21)

# # print(House1.street)
# # print(House2.number)
        
# # House1.build()

# # print(House1.age)

# # House2.age_of_house(5)
# # print(House2.age)

# PrHouse = ProspectHouse('Ленина', 5)
# print(PrHouse.prospect)
#----------------------------
# Множества

# numbers = {1, 2, 3, 4, 5} # множество
# numbers2 = {2, 6, 54, 42, 34, 5}

# numbers.add(58) #добавит в конец множества элемент 58
# numbers.discard(58) # удаление элемента 58 (если такого нет он ничего не напишет)
# numbers.remove(58) # удаление элемента 58 (если такого нет, выдаст ошибку)
# numbers.pop() # удалит первый элемент множества
# numbers.clear() # удалит все элементы в множестве
# len(numbers) # количество элементов в первом множестве
# numbers3 = numbers.union(numbers2) # объединит все элементы двух множеств
# numbers3 = numbers | numbers2 # объединит все элементы двух множеств
# numbers3 = numbers.intersection(numbers2) # объединит тольео те элементы которые совподают в первом и во втором множестве (пересечение)
# numbers3 = numbers & numbers2 # объединит тольео те элементы которые совподают в первом и во втором множестве (пересечение)
# numbers3 = numbers - numbers2 # разница множеств
# numbers3 = numbers2.copy() # копирует элементы из 2рого множества в 3тье
# ----------------
# Регулярные выражения - шаблон по которому осуществляется поиск

# import re # подключение модуля для работы с регулярными выражениями

# s = 'AC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DC'
# # result = re.match('AC', s) # re.match() поиск в начале строки
# # result = re.search('DC', s) # re.search() поиск по всей строке и вывод первого встречного
# # result = re.findall('DC', s) # re.findall() поиск по всей строке и создание списка из найденных элементов
# # result = re.split('/', s) # re.split() разделяет строку по заданному элементу и записывает в список
# # result = re.split('/', s, maxsplit=3) # третий аргумент в split() позволяет задать по сколько элементов ограничесть задонного элемента
# # result = re.sub('A', 'D', s) # re.sub()замена первого аргумента на второй аргумент в строке
# result = re.fullmatch('A', s) # re.fullmatch() является заданный аргумент полный строчкой(в данном случае НЕТ)
# print(result)

# s = '4543+435340        ------ dklfbkldg8448131^3 HHKLNKN:Ll;kkdas'
# result = re.search(r'd..f', s)# точка это один любой символ в строке. Результат dklf
# result = re.search(r'\d\d\d\d\d', s) # \d выведет цифру 
# result = re.search(r'\d{3}', s) # чтоб не указываеть куча одинаковых \d можно воспользоваться {}, цифра в внутри указывает сколько раз повторять
# result = re.search(r'\d{1,3}', s) # можно указывать диапозон
# result = re.search(r'\d{2,}', s) # немение двух повторения
# result = re.search(r'\d{,2}', s) # неболее двух повторения
# result = re.search(r'\D', s) # \D вывод символа кроме цифры
# result = re.search(r'\s', s)# табуляция, пробел
# result = re.search(r'\S', s)# любой символ кроме табуляция, пробел
# result = re.search(r'\w', s) # любая цифра, буква или нижние подчеркивание
# result = re.search(r'\W', s) # любая не цифра, не буква или не нижние подчеркивание
# result = re.search(r'\bHH', s) # начало нового слова
# result = re.search(r'\BHH', s) # не начало нового слова
# result = re.search(r'[afghjk]', s) # набор или диапозон символов. Ищет по заданному в строке первый найденный символ
# result = re.search(r'[1-5]', s) # заданный диапозон и вывод первой найденной цифры в этом диапозоне
# result = re.search(r'[^1-3]', s) # вывести цифру которая в не диапозон
# result = re.search(r'H|l', s) # то что найдет раньше
# print(result)

# s = 'Привет! Как дела? А у меня нормально.'
# result = re.findall(r'[бвгджзклмнпрстфхцчшщБВГДЖЗКЛМНПРСТФХЦЧШЩ]\w+',s)
# print(result)
#----------------------------------
# lambda (неназванная функция)

# def rectangle_area(a, b):
#     return a * b
# print(rectangle_area(4, 5))

# print((lambda a, b: a * b)(4, 5))# тоже самое что и выше через функцию, но через lambda

# def maximum(a, b):
#     if a > b:
#         return a
#     else:
#         return b
# print(maximum(25, 17))

# print((lambda a, b: a if a > b else b)(25, 17))# вернуть a если a > b, в противном случае вернуть b
#--------------------
# Функции Map, Filter, Reduce, Zip
# Функция map(), принимает два аргумента функцию и итерируемую последовательность

# with open('map.txt') as file:
#     n = int(file.readline())
#     for i in range(n):
#         a, b = map(int, file.readline().split())
#         print(a, b)

# def f(a, b):
#     return a * b

# a = map(f, [2, 4, 5], [5, 6, 7])
# print(list(a))

# print(list(map(lambda x: x + 15, (2, 4, 5))))

#Функция filter()- первый аргумент функция, второй последовательность к котрой приминяется функция

# def f(a):
#     if a % 2 == 0:
#         return a
# a = filter(f, (2, 4, 5))
# print(list(a))


# print(list(filter(lambda a: a % 2 == 0, (2, 4, 5))))

#Функция reduce()- первый аргумент функция

# from functools import reduce

# print(reduce(lambda a, b: a + b, (50, 57, 89, 12, 100)))

#Функция zip()- объединяет итерируемые объекты в кортедж

# a = [1, 2, 3, 4, 5, 6]
# b = 'abcdef'
# result = zip(a, b)
# print(list(result))
# --------------------
# # Виды аргументов

# def arg(a, b, c=8):
#     print(a, b, c)
# arg(1, 2)
# #в таком случае будет использоваться тот аргумент (С) который был задан в функции
# arg(1, 2, 3)
# # #в этос случае заданое значение в функйии игнорируется и заменяется тем значение которое мы направляем в функцию
# arg(c=3, a=1, b=2)
# # #в этом случае посылаемые значения именнованные, хоть они не попорядку но они соответствуеют имени аргументам в функции

# def summa(*numbers): # *numbers(* и любое имя) - аргумент которорый позволяет использовать любое количество аргументов
#     print(sum(numbers))
# summa(7, 8, 9, 1, 2, 3)

# def brand(**brands): #** именнованый аргумент сколько захочешь. Выводит как словарь
#     print(brands)
# brand(a='Apple', s='Samsung')
# -------------------
# Генераторы списков, множеств и словарей
# s = []
# for i in range(1, 21):
#     if i % 5 == 0:
#         s.append(i)
# print(s)

# s1 = [i for i in range(1, 21) if i % 5 == 0]
# print(s1)

# s = []
# for i in range(1, 21):
#     for j in range(1, 51):
#         s.append((i, j))
# print(s)

# s1 = [(i, j) for i in range(1,21) for j in range(1,51)]
# print(s1)

# s = []
# for i in range(-10, 11):
#     if i > 0:
#         s.append(i**2)
#     else:
#         s.append(i**3)
# print(s)

# s1 = [i**2 if i > 0 else i **3 for i in range(-10, 11) ]
# print(s1)
# s2 = [i**2 if i > 0 else i **3 for i in range(-10, 11) if i % 2 == 0]
# print(s2)

# s = [7, 8, 8, -10, -10, 9]
# set_set = {i for i in s}
# print(set_set)

# dictionary = {i: i ** 10 for i in s}
# print(dictionary)
#---------------------
# Вложенные функции, замыкание

# import builtins
# print(dir(builtins)) # выведет все зарезервированые именя программой

# y = 2
# def degree(x):
#     return y ** x
# print(degree(4))

def message(number):
    def print_message():
        return 'Число ' + str(number)
    return print_message()
print(message(78))

