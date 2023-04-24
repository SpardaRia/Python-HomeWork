def menu() -> int:
    
    print('1 - Вывести весь справочник;\n2 - Найти абонента по фамилии и/или изменить данные;\n'
          '3 - Найти абонента по номеру телефона;\n4 - Ввести данные нового абонента;\n5 - Сохранить;\n6 - Завершить работу.')
    print('Введите число для операции со справочником:')
    number = int(input())
    return number


def show_menu2() -> int:
    print('Введите число для операции со справочником:')
    print('1 - Удалить абонент;\n2 - Изменить Фамилию;\n'
          '3 - Изменить Имя;\n4 - Изменить Номер телефона;\n6 - Вернуться.')
    number = int(input())
    return number


def read_csv(spisok: str):
    data = []
    abonent = ["Фамилия", "Имя", "Телефон", "Описание"]
    
    with open(spisok, 'r', encoding='utf-8') as file:
        for line in file:
            data.append(dict(zip(abonent, line.strip().split(','))))
    return data



def display_all_records(spisok: list):
    for qwer in spisok:
        for k, v in qwer.items():
            print(f'{k}: {v}')
        print()
    input("Нажмите Enter ")
    print()




def find_last_name(spisok):
    family = input("Введите фамилию: ")
    print()
    count = 0
    indexAbonent = 0
    abonent = []
    for qwer in spisok:
        if family in qwer['Фамилия']: 
            count += 1
            abonent.append(qwer)
            print(f'{count}: ')
            for k, v in qwer.items():
                print(f'{k}: {v}')
            print()
    if count > 1:
        indexAbonent = int(input("Найдено более одного абонента\n"
                          "Для возвращения нажмите 0\n"
                          "Для изменения данный нажмите номер абонента из списка: "))
        if indexAbonent > 0:
            count = 1
            indexAbonent = indexAbonent - 1
            print()
    if count == 1:
        number = 0
        while number != 6:
            number = show_menu2()
            if number == 1:
                spisok.remove(abonent[indexAbonent])
                print("Абонент удалён\n")
            if number == 2:
                abonent[indexAbonent]['Фамилия'] = input(
                    "Введите новую Фамилию: ")
                print("Измененно\n")
            if number == 3:
                abonent[indexAbonent]['Имя'] = input("Введите новое Имя: ")
                print("Изменено\n")
            if number == 4:
                abonent[indexAbonent]['Телефон'] = input(
                    "Введите новый телефон: ")
                print("Изменено\n")
            if number == 5:
                abonent[indexAbonent]['Описание'] = input(
                    "Введите новое описание: ")
                print("Изменено\n")

    if count == 0:
        print("Такой фамилии нет")
        print()
        input("Нажмите Enter ")


def find_phone_number(spisok):
    telephone = input("Введите номер телефон: ")
    count = 0
    for qwert in spisok:
        if qwert['Телефон'] == telephone:
            count += 1
            for k, v in qwert.items():
                print(f'{k}: {v}')
            print()
    if count == 0:
        print("Номер телефона не найден")
        print()
    input("Нажмите Enter")


def add_data(spisok):
    list = []
    fields = ["Фамилия", "Имя", "Телефон", "Описание"]
    list.append(input("Введите фамилию: "))
    list.append(input("Введите имя: "))
    list.append(input("Введите телефон: "))
    list.append(input("Введите описание: "))
    new_abonent = dict(zip(fields, list))
    spisok.append(new_abonent)
    print()
    print("Добавленно: ")
    for k, v in new_abonent.items():
        print(f'{k}: {v}')
    print()
    input("Нажмите Enter")


def saveSpisok(spisok):
    with open(input("Имя файла: "), 'w', encoding='utf-8') as new_file:
        for qwert in spisok:
            for k, v in qwert.items():
                new_file.write(f'{k}: {v}\n')
            new_file.write("\n")
    print("Сохраненно")


spisok = read_csv(r'D:\School\Python\S08\phonebook.csv')

number = 0
while number != 6:
    number = menu()
    if number == 1:
        display_all_records(spisok)
    if number == 2:
        find_last_name(spisok)
    if number == 3:
        find_phone_number(spisok)
    if number == 4:
        add_data(spisok)
    if number == 5:
        saveSpisok(spisok)