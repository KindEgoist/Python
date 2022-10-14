# Задача 5
# Задайте двумерный массив из целых чисел. Количество строк и столбцов задается с клавиатуры. Отсортировать элементы по возрастанию слева направо и сверху вниз.
# Например, задан массив:
# 1 4 7 2
# 5 9 10 3
# После сортировки
# 1 2 3 4
# 5 7 9 10

from random import randint # модель случайных чисел

stroka = int(input('Введите количество строк: '))
stolbec = int(input('Введите количество столбцов: '))
min = int(input('Введите Минимальное значение: '))
max = int(input('Введите Максимальное значение: '))

list2d = [[randint(min, max) for j in range(stolbec)] for i in range(stroka)]

for i in range(stroka):
    for j in range (stolbec):
        print(list2d[i][j], end= ' ')
    print()
    
print('Сортировка: ')
for m in range(stroka * (stroka-1)):
    for i in range(stroka):
        for n in range(stolbec):
            for j in range (stolbec-1):
                if list2d[i][j] > list2d[i][j+1]:
                    temp = list2d[i][j]
                    list2d[i][j] = list2d[i][j+1]
                    list2d[i][j+1] = temp           

    for i in range(stroka-1):
        if list2d[i][-1] > list2d[i+1][0]:
            temp = list2d[i][-1]
            list2d[i][-1] = list2d[i+1][0]
            list2d[i+1][0] = temp

for i in range(stroka):
    for j in range (stolbec):
        print(list2d[i][j], end= ' ')
    print()