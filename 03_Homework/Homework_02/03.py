# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов 
# на указанных ИНДЕКСАХ. Пять ИНДЕКСОВ хранятся в списке, который вы сами заполняете.
# Пример списка ИНДЕКСОВ [2, 4, 3, 1, 8]
# Ввод: 10
# [-10, -9, ...-4, -3, -2, -1, 0, 1, 2, 3,4....10]

try:
    num = int(input('Введите число N: '))
    list = []
    for i in range(num * 2 + 1):
        list.append (-num + i)
    print (f'Получен первый список от {-num} до {num}: {list}')

    list2 = []
    for i in range(5):
        list2.append (int(input(f'Введите {i + 1} число: ')))
    print (f'Получен второй список: {list2}')

    proizvedenie = 1
    for i in range(len(list2)):
        index = list2[i]
        proizvedenie *= list[index]
    print (f'Результат произведений: {proizvedenie}')
except:
    print('Вводите только ЧИСЛА!')
