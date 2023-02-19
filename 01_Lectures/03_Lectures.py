# lambda ананимная функция(неопраделена)

# def f(x):
#     return x**2

# g = f # в переменную g положили всю функцию f (переменная которая хранит ссылку на функцию)

# print(type(f))
# print(type(g))

# print(f(4))
# print(g(4))


# def calc(x):
#     return x + 10
# # print(calc(10))

# def calc2(x):
#     return x*10
# # print(calc2(10))

# def math(op,x):
#     print(op(x))
# math(calc2, 10)
# math(calc, 10)

# def sum(x, y):
#     return x + y
# sum = lambda x, y: x + y # здесь написано все тоже самое что и выше функция sum 

# def mylt(x, y):
#     return x * y

# def calc(op, a, b): # в качестве аргумента может выступать целая функция
#     print(op(a, b))
#     # return op(a,b)

# calc(sum, 4, 5)
# calc(lambda x, y: x + y + 1, 4, 5) # вариант без переменной sum

# List Comprehension

# list = []
# for i in range(1, 101):
#     if(i % 2 == 0):
#         list.append(i)
# print(list)

# list = [i for i in range (1, 21)] # вид записи заполнения списка от 1 до 20
# list2 = [i for i in range (1, 21) if i % 2 == 0] # вывод четных 
# list3 = [(i, i) for i in range (1, 21) if i % 2 == 0] # кортеджи
# print(list)
# print(list2)
# print(list3)

# def f(x):
#     return x**3
# list4 = [f(i) for i in range (1, 21) if i % 2 == 0]
# print (list4)
# list5 = [(i, f(i)) for i in range (1, 21) if i % 2 == 0]
# print (list5)

# path = 'D:\Python\01_Lectures\Lectures_03\1.txt'
# f = open(path, 'r') 
# data = f.read() + ' '
# f.close()

# number = []

# while data != ' ':
#     space_pos = data.index(' ')
#     number.append(int(data[:space_pos]))
#     data = data[:space_pos + 1:]

# out = []
# for e in number:
#     if not e % 2:
#         out.append((e, e ** 2))
# print(out)

# def select(f, col):
#     return [f(x) for x in col]

# def where(f,col):
#     return [x for x in col if f(x)]

# data = '1 2 3 5 8 15 23 38'.split()

# res = select(int, data)
# print(res)
# res = where(lambda x: not x % 2, res)
# res = select(lambda x: (x, x**2), res)
# print(res)

# Функция map применяет указанную функцию к каждому элементу итерируемого объекта и возращает итератор с новыми объектоми

# li = [x for x in range(1, 20)]
# li = list(map(lambda x: x + 10, li))
# print(li)

# data = list(map(int,input().split()))
# print(data)


# data = list(map(int,'1 2 3'.split()))
# for e in data:
#     print(e)
# print('-----')
# for e in data:
#     print(e)



# def where(f,col):
#     return [x for x in col if f(x)]

# data = '1 2 3 5 8 15 23 38'.split()

# res = list(map(int, data))
# print(res)
# res = where(lambda x: not x % 2, res)
# res = list(map(lambda x: (x, x**2), res))
# print(res)

# Функция filter() применяет указанную функцию к каждому элементу интерируемого объекта и возвращает итератор с теми объектами,для которых функция вернула True.

# data = [x for x in range(10)]
# res = list(filter(lambda x: not x % 2, data))
# print(res)

# data = '1 2 3 5 8 15 23 38'.split()

# res = list(map(int, data))
# print(res)
# res = filter(lambda x: not x % 2, res)
# res = list(map(lambda x: (x, x**2), res))
# print(res)

# Функция zip() применяется к набору итерируемых объектов и возвращает итератор с кортежами из элементов входных данных
from itertools import zip_longest
users = ['users1', 'users2', 'users3', 'users4', 'users5', 'users5']
ids = [4, 6, 9, 14, 7]
# data= list(zip(users, ids))
data = list(zip_longest(users, ids, fillvalue= ids))
print(data)

# Функция enumerate() применяется к итерируемому объекту и возвращает новый итератор с кортежами из индекса и элементов входных данных.

# users = ['users1', 'users2', 'users3', 'users4', 'users5']

# data= list(enumerate(users))
# print(data)