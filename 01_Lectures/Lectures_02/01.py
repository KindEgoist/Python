#Запись и перезапись

# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'a') #переменная data. open()-открыть. файл file.txt и модификатор а
# data.writelines(colors) #производим запись .разделителей не будет
# data.close #разрыв соединения


# data = open('file.txt', 'a') 
# data.write('\nLINE 2\n')
# data.write('LINE 3\n')
# data.close

# with open('file.txt', 'w') as data: # создает и принимать в переменную data (as data) выше стояющию конструкцию open('file.txt', 'w')
#     data.write('\nLine 2\n')
#     data.write('Line 3\n') # в конце автоматически сделает разрыв соединения 

#Чтение файла

# path = 'file.txt' #путь к файлу
# data = open(path, 'r') # чтение
# for line in data: # c помощью цикла пробегаем по файлу и считываем все строки
#     print(line)
# data.close()

# Импорт

# import funF as h #импортируем файл как модуль из тойжу папки где находимся. переменовали funF в h. В дальнейшем обращаемся вместо funF по h
# print(h.f(1))

# Работа с функциями и ее аргументами

# def new_string(symbol, count = 3):
#     return symbol * count
# print(new_string('!', 5)) # !!!!! 
# print(new_string('!')) # !!!
# print(new_string(4)) # 12

def concatanatio(*params): # *- позволяет добавить аргументы
    res: str = "" # присваеваем к переменной res тип строки
    for item in params:
        res += item
    return res

print(concatanatio('a', 's', 'd', 'w')) # asdw
print(concatanatio('a', '1')) #a1
#print(concatanatio(1, 2, 3, 4))
