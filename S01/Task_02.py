# Задача 2: Найдите сумму цифр трехзначного числа. 

# *Пример:*

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

while True:
    userNumber = input ('Введите трехзначное число: ')
    lengthNumber = len(userNumber)
    if lengthNumber == 3:
            print('Верно')
            sum = int(userNumber[0]) + int(userNumber[1]) + int(userNumber[2])
            print(sum)
            break
    else:
        print('Введено неверное число')
