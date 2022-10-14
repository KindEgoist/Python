# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# import math

# num = int(input('Введите число N: '))

# list = []
# for i in range(num):
#     list.append(math.factorial(i + 1))
  
# print (list)



try:
    num = int(input('Введите число N: '))

    list = []
    fac = 1
    for i in range(num):
        list.append(i + 1)
    print (f'Полученный список: {list}')

    for i in range(len(list)):
        fac *= (i + 1)
        list[i] = fac 
    print (f'Преобразованный список: {list}')
except:
    print('Введите ЧИСЛО!')
