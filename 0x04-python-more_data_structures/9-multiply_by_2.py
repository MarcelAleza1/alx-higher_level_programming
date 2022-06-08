#!/usr/bin/python3
def mulitply_by_2(my_dict):
    dict1 = {}
    for x, y in my_dict.items():
        dict1.update({x: (y * 2)})
    return dict1
