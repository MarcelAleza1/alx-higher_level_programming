#!/usr/bin/python3
def complex_delete(my_dict, value):
    dict1 = my_dict.copy()
    for x, y in dict1.items():
        if value == y:
            my_dict.pop(x)
    return my_dict
