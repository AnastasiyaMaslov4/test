

def search_user(data):
    search_char = input("Введите данные для поиска: ")
    find = False
    for user in data:
        if search_char in user['ФИО']:
            print("------------------------------------------\n")
            print(user)
            print("------------------------------------------\n")
            find = True
    if not find:
        print("------------------------------------------\n")
        print(" \033[31m Пользователь не найден \033[0m " )
        print("------------------------------------------\n")
    