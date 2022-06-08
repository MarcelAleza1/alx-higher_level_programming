#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """
    function to replace all occurences
    of an element in a new list
    """
    result = []
    for x in my_list:
        if x == search:
            result.append(replace)
        else:
            result.append(x)
    return result
