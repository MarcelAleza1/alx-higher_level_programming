#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    sum1 = sum([x * y for (x, y) in my_list])
    sum2 = sum([y for (x, y) in my_list])
    return sum1 / sum2
