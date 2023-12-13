import requests

from main import ClientsMod

while True:
    choise = int(input("Выберите c кем работать будем (1)Клиент (2)КонстрактМатериалы (3)ФинишМатериалы: "))

    if choise == 1:
        choise = int(input("Выберите действие с Клиентом (1)Get (2)Post (3)Put (4)Delete: "))

        if choise == 1:
            choise = int(input("Введите id: "))
            r = requests.get(f'http://127.0.0.1:8000/getClient/{choise}')
            print(r.content)
            print(r.status_code)
        elif choise == 2:
            a1 = input("Введите имя: ")
            a2 = input("Введите фамилию: ")
            a3 = input("Введите отчество: ")
            a4 = input("Введите номер телефона: ")
            a5 = input("Введите логин: ")
            a6 = input("Введите пароль: ")
            r = requests.post(f'http://127.0.0.1:8000/postClient?ClientName={a1}&ClientSurname={a2}&ClientPatronymic={a3}&phoneNumber={a4}&Client_login={a5}&Client_pswd={a6}')
            print(r.status_code)
        elif choise == 3:
            choise = int(input("Введите id: "))
            a1 = input("Введите имя: ")
            a2 = input("Введите фамилию: ")
            a3 = input("Введите отчество: ")
            a4 = input("Введите номер телефона: ")
            a5 = input("Введите логин: ")
            a6 = input("Введите пароль: ")
            r = requests.put(
                f'http://127.0.0.1:8000/putClient/{choise}?ClientName={a1}&ClientSurname={a2}&ClientPatronymic={a3}&phoneNumber={a4}&Client_login={a5}&Client_pswd={a6}')
            print(r.status_code)
        elif choise == 4:
            choise = int(input("Введите id: "))
            r = requests.delete(f'http://127.0.0.1:8000/delClient?id={choise}')
            print(r.status_code)

    elif choise == 2:
        choise = int(input("Выберите действие с Клиентом (1)Get (2)Post (3)Put (4)Delete: "))

        if choise == 1:
            choise = int(input("Введите id: "))
            r = requests.get(f'http://127.0.0.1:8000/getCM/{choise}')
            print(r.content)
            print(r.status_code)
        elif choise == 2:
            a1 = input("Введите название: ")
            a2 = input("Введите количество: ")
            r = requests.post(
                f'http://127.0.0.1:8000/postCM?MaterialName={a1}&Quantity={a2}')
            print(r.status_code)
        elif choise == 3:
            choise = int(input("Введите id: "))
            a1 = input("Введите название: ")
            a2 = input("Введите количество: ")
            r = requests.put(
                f'http://127.0.0.1:8000/putCM/{choise}?MaterialName={a1}&Quantity={a2}')
            print(r.status_code)
        elif choise == 4:
            choise = int(input("Введите id: "))
            r = requests.delete(f'http://127.0.0.1:8000/delCM?id={choise}')
            print(r.status_code)
    elif choise == 3:
        choise = int(input("Выберите действие с Клиентом (1)Get (2)Post (3)Put (4)Delete: "))

        if choise == 1:
            choise = int(input("Введите id: "))
            r = requests.get(f'http://127.0.0.1:8000/getFM/{choise}')
            print(r.content)
            print(r.status_code)
        elif choise == 2:
            a1 = input("Введите название: ")
            a2 = input("Введите количество: ")
            r = requests.post(
                f'http://127.0.0.1:8000/postFM?MaterialName={a1}&Quantity={a2}')
            print(r.status_code)
        elif choise == 3:
            choise = int(input("Введите id: "))
            a1 = input("Введите название: ")
            a2 = input("Введите количество: ")
            r = requests.put(
                f'http://127.0.0.1:8000/putFM/{choise}?MaterialName={a1}&Quantity={a2}')
            print(r.status_code)
        elif choise == 4:
            choise = int(input("Введите id: "))
            r = requests.delete(f'http://127.0.0.1:8000/delFM?id={choise}')
            print(r.status_code)


