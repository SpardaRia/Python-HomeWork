# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.

# *Пример:*

# 385916 -> yes
# 123456 -> no

n = input ('Введите шестизначное число: ')

if len(n) == 6:
    q = int(n[0]) + int (n[1]) + int(n[2])
    g = int(n[3]) + int (n[4]) + int(n[5])

    if q == g:
        print('Поздравляю! У вас счастливый билет')
    else:
        print('Ваш билет не счастливый')
        
else:
    print('Введено некоректное число')