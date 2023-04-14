'''Задача 30:  Заполните массив элементами арифметической прогрессии. 
Её первый элемент, разность и количество элементов нужно ввести 
с клавиатуры. Формула для получения n-го члена прогрессии: 
    an = a1 + (n-1) * d.
Каждое число вводится с новой строки.    
'''
a = int(input('Введи с кокго элемента начинать прогрессию: '))
d = int(input('Введи шаг прогрессии: '))
n = int(input('Введи количество чисел: '))    

list_progresia = []

for i in range(n):
    an = a + i * d
    list_progresia.append(an)

print(list_progresia)


# a = int(input('Введи с кокго элемента начинать прогрессию: '))
# d = int(input('Введи шаг прогрессии: '))
# n = int(input('Введи количество чисел: '))    

# list_progresia = [a]

# num = a

# for i in range(n-1):
#     num = num + d
#     list_progresia.append(num)
    
# print(list_progresia)
