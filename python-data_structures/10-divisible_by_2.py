#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    new_ruslt = []
    for num in my_list:
        if num % 2 == 0:
            new_ruslt.append(True)
        else:
            new_ruslt.append(False)
    return new_ruslt
