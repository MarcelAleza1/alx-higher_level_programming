#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    flag = 0
    for i in range(0, x):
        try:
            print("{}".format(my_list[i]), end="")
            flag += 1
        except (ValueError, TypeError, IndexError):
            break
    print()
    return flag
