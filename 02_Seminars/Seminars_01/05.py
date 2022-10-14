# Напишите программу, которая принимает на вход число и проверяет, кратно ли оно 5 и 10 или 15, но не 30.
# try:
#     numbers = int(input('Введите число: '))
#     if numbers % 5 == 0  and numbers % 10 == 0:
#         print(f'Число {numbers} крастно 5 и 10')
#     elif numbers % 15 == 0 and numbers % 30 != 0:
#         print(f'Число {numbers} крастно 15 но не кратно 30')
#     else:
#         print(f'Число {numbers} не удовлетворяет не одному условию')
# except:
#     print('Введите число')
    
try:
    numbers = int(input('Введите число: '))
    if (numbers % 5 == 0 and numbers % 10 == 0 or numbers % 15 == 0) and numbers % 30 != 0:
        print(f'Число {numbers} удовлетворяет условию')
    else:
        print(f'Число {numbers} не удовлетворяет условию')
except:
    print('Введите число')