# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, причем кусты высажены только по окружности. 
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, находясь перед некоторым 
# кустом заданной во входном файле грядки.

un = int(input('Укажите колличество кустов: '))

#kyst = []

from random import randint

# for i in range(un):
#     kyst.append(randint(1, 10))
#     print(kyst[i])
# print()

kyst = [randint(1, 10) for i in range(un)]
print(*kyst)

# ind = 0
finSum = 0

for i in range(len(kyst)):
    sum = kyst[i-2] + kyst[i-1] + kyst[i]
    if sum > finSum:
        finSum = sum


# for j in kyst:
#     if ind == 0:
#         sum = kyst[-1] + kyst[0] + kyst[1]
      
#     elif ind == (un-1):
#         sum = kyst[un-2] + kyst[un-1] + kyst[0]
       
#     else:
#         sum = kyst[ind-1] + kyst[ind] + kyst[ind+1]

#     if sum > finSum:
#         finSum = sum
#     ind += 1

print(f'Максимальное колличество ягод: {finSum}')