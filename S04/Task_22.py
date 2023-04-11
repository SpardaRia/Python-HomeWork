# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.



spisk1 = []
spisk2 = []

from random import randint

n = int(input('Введите количество чисел в первом множестве: '))
spisk1 = [randint(1, 10) for i in range(n)]
print(*spisk1)

# Если заполнять множества вручную (список 1)
# print('Заполните первый список: ')
# for i in range(n):
#     spisk1.append(input(f'Элемент {i+1}: '))

m = int(input('Введите количество чисел во втором множестве: '))
spisk2 = [randint(1, 10) for i in range(m)]
print(*spisk2)

# Если заполнять множества вручную (список 2)
# print('Заполните второй список: ')
# for i in range(m):
#     spisk2.append(input(f'Элемент {i+1}: '))

kort1 = set(spisk1)
kort2 = set(spisk2)

qwert = kort1.intersection(kort2)
print(*qwert)
# qwert = list(qwert)


# qwert.sort(reverse=False)
# print(f'sort {qwert}')




