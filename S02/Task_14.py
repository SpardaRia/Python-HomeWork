# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

userNumber = int(input('Введите число: '))
g = 1
while userNumber >= g:
    print(g, end=' ')    
    g = g*2    