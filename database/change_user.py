

def change_user(data):
    user = input("Введите ФИО пользователя, котрого коснутся изменения: ")
    key = input("Введите название поля, в которое хотите внести изменения: ")
    change_user = None
    for i in data:
        if user in i['ФИО']:
            change_user = i
            new_key = None
            new_key = input("Введите новые данные: ")
            change_user[key] = new_key
    if not change_user:
        print("------------------------------------------\n")
        print(" \033[31m Пользователь не найден \033[0m ")
        print("------------------------------------------\n")
    return data