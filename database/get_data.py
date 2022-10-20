from pprint import pprint


def get_data(data):
    print("------------------------------------------\n")
    for user in data:
      pprint(user, sort_dicts=False) 
      print("------------------------------------------\n")