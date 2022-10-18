# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

try:
    len = int (input('Введите длину списка: '))
    list = []
    list2 =[]
    for i in range (len):
        list.append (int(input(f'Введите {i + 1} число: ')))
    print()
    print(f'Список: {list}')

    if len % 2 == 0:
        len = int(len / 2)
    else:
        len = int((len / 2) + 1)

    for i in range(len):
        list2.append (list[i] * (list [-1 - i]))
    print(f'Произведение пар: {list2}')
except:
    print('Введите целое число!')
