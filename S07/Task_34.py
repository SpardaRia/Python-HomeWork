
# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его кричалках 
# не настолько просто, насколько легко он их придумывает, Вам стоит написать программу. Винни-Пух считает, 
# что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. 
# Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами. 
# Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух вбивает в программу с клавиатуры. 
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке

# *Пример:*

# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да    
#     **Вывод:** Парам пам-пам  


def is_vowel(c):
    c = c.split()
    list_1 = []
    for word in c:
        summa = 0
        for i in word:
            if i in 'ауоыиэяюёеaeiou':
                summa += 1
        list_1.append(summa)
    return len(list_1) == list_1.count(list_1[0])


qwert = 'пара-ра-рам рам-папам па-ра-па-дам'

if is_vowel(qwert):
    print('Парам пам-пам')
else:
    print('Пам парам')




# def is_vowel(c):
#     count = 0
#     hi = 0
#     if c.lower() in 'ауоыиэяюёеaeiou':
#         for i in c:
#             if c[hi].lower() in 'ауоыиэяюёеaeiou':
#                 count += 1
#                 hi += 1
#                 print(f'count = {count}')
#                 return count
#     return 1
            
    
# qwert = str(input('Введите текст, разделяя слоги в словах через "-": '))

# qwert = qwert.replace('-', '')
# print(qwert)


# if all(map(lambda x: is_vowel(qwert) % 2 == 0, qwert)):
#     print('Парам пам-пам')
# else:
#     print('Пам парам')




# alp = "аеёиоуыэюя"
# word_sug = input().split()
# vowel_letters = [sum([True for j in word if j.lower() in alp]) for word in word_sug]

# if all(vowel_letters) and len(set(vowel_letters)) == 1:
#     print("Парам пам-пам")
# else:
#     print("Пам парам")

