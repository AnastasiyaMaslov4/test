import menu
import jf
import add_key as ak
import get_data as gd
import add_user as au
import search_user as su
import change_user as cu



# def initialization():
#     file = os.path.isfile("data_file.json")
#     if file == False:
#         data = []
#         js.write_in_file(data)
#     # чтение существующего файла
#     data = js.read_file()
#     return data

def data_comm():
    data = jf.read_file()
    exit = True
    while exit:
        what = menu.menu()
        if what == 1:
            gd.get_data(data)
        elif what == 2:
            ak.get_add_key(data)
        elif what == 3:
            au.get_add_user(data)
        elif what == 4:
            cu.change_user(data)
        elif what == 5:
            su.search_user(data)
        else:
            jf.write_in_file(data)
            exit = False
    return data