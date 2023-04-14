''' Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую 
сумму двух целых неотрицательных чисел. Из всех арифметических 
операций допускаются только +1 и -1. Также нельзя использовать 
циклы.

*Пример:*

2 2
    4 
'''

def summa(a1, b2):
    if b2 == 0:
        return a1
    return a1 + summa(1, b2-1)

userNumber1 = int(input('Введите число 1: '))
userNumber2 = int(input('Введите число 2: '))

print(f'{userNumber1} + {userNumber2} = {summa(userNumber1, userNumber2)}')
