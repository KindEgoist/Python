# Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
# Примеры:
# - 1, 4, 8, 7, 5 -> 8
# - 78, 55, 36, 90, 2 -> 90
try:
    def create_list():
        list = []  
        for i in range(5):
            list.append(int(input(f'Введите {i+1} число: ')))
        return list
        
    def find_max(list):
        max = list[0]
        for i in range(len(list)):
            if list[i] > max:
                max = list[i]
        return max

    res = create_list()          
    print(res)
    max = find_max(res)
    print(max) 
except:
    print('Введите целое число')
