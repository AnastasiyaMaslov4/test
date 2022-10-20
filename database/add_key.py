


def get_add_key(data):
    user_key = input('Введите название нового поля: ')
    for x in data:
        x[user_key] = '*'
    return data

