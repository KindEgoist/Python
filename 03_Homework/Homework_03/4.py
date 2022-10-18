# Задайте число N. Составьте список чисел Фибоначчи, N - количество чисел в списке


try:
    size = int(input('Введите количество чисел в списке: '))
    num1 = int(input('Введите первое число: '))
    num2 = int(input('Введите второе число: '))

    list = [num1, num2]
    for i in range(size - 2):
        list.append(list[i]+list[i + 1])
    print(f'Список чисел Фибоначчи: {list}')
except:
    print('Введите число')
