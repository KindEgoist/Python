# Петя и Катя - брат и сестра. Петя - студент, а Катя - школьница. Петя помогает Кате по математике.
# Он задумывает два натуральных числ а Катя должна их отгадать.
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение Р
# Помогите Кате отгадать задуманные Петей числа.
# *Пример*
# Ввод: 4 4
# Вывод: 2 2
# *Пример*
# Ввод: 5 6
# Вывод: 2 3

from re import I


def find(summa, proizvedenie):
    for i in range(1, summa+1):
        for j in range(1, summa+1):
            if summa == i + j and proizvedenie == i * j:
                return i, j
    return None
            
summa = int(input('Введите число сыммы: '))
proizvedenie = int(input('Введите число произведения: '))
result = find(summa, proizvedenie)
print (f'Числа: {result[0]} {result[1]}') if result != None else print('Числа не найдены')

sum = int(input())
proiz = int(input())
for i in range(sum):
    if i * (sum - i) == proiz:
        x = i
        y = sum - i
print (x, y)