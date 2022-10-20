from data_comm import data_comm
from menu import menu
import jf
import os.path

def initialization():
    file = os.path.isfile("data_file.json")
    if file == False:
        data = []
        jf.write_in_file(data)
    data = jf.read_file()
    return data

initialization()

data_comm()