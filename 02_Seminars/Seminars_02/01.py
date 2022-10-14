# Найти Максимальный элемент в списке из 5 элементов
# Пример
# 3 -6 10 23 -14
# ответ 23

list = [3, -6, 10, 23, 58]
max = list[0]
for i in range(len(list)):
    if list[i] > max:
        max = list[i]
print (f'Макс = {max}')