# Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число


# def finder (list, number):
#     for i in list:
#         if i.find(number) >=0:
#             return 'Да'
#     return 'Нет'

# list = ['строка 1', 'строка' 'строка 3' 'строка' '13']
# number = input('Введите число: ')
# print(finder(list,number))

list = ['строка 1', 'строка' 'строка 3' 'строка' '13']
number = input('Введите число: ')
for i in list:
    if number in i:
        i = True
        break
    else: i = False
print (i)
