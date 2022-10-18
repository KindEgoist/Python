# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

try:
    def dvoichnaya(num):
        if num == 0:
            return 0
        else:
            list = []
            while num >= 1:
                list.insert(0, int(num % 2))
                num = num / 2
            return list    
 
    num = float (input('Введите число: '))
   
    print(*dvoichnaya(num))
except:
    print('Введите число')


