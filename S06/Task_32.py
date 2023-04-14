''' Задача 32: Определить индексы элементов массива (списка), 
значения которых принадлежат заданному диапазону 
(т.е. не меньше заданного минимума и не больше заданного максимума)
Ввод:  [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
5
15
Вывод: [1, 9, 13, 14, 19] '''

from random import randint as rnd

list = [rnd(0, 10) for _ in range(10)]
print(list)

n = int(input('Введите первое число диапозона: '))
m = int(input('Введите второе число диапозона: '))

if n < m:
    max_num = m
    min_num = n
else:
    max_num = n
    min_num = m
    print(f'max_num = {max_num} min_num = {min_num}')
    
ind = 0
list_ind = []

for i in list:
    if i >= min_num and i <= max_num:
        list_ind.append(ind)
    ind += 1
    
print(list_ind)
