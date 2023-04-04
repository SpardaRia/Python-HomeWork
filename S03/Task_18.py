# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. Пользователь в первой строке вводит натуральное число 
# N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X 
# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5


n = int(input('Введите колличество элементов: '))

from random import randint
nubmerList = [randint(1, 100) for i in range(n)]

print(nubmerList)

x = int(input('введи искомое число: '))

print(nubmerList)

index = 1
qwert = abs(x - nubmerList[0]) # для снятия ограничения размера искомого числа
# qwert = 100 при поиске числа больше 100 выдаст 0
requiredNumber = nubmerList[0]

for j in nubmerList[1:]:
    
    if (abs(x - nubmerList[index])) <= qwert:
        requiredNumber = nubmerList[index]
        qwert = abs(x - nubmerList[index])

    index += 1
print(requiredNumber) 

