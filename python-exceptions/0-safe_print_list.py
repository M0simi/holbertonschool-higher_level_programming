#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
            print(my_list[i], end="")  # prinnt with out new line
            count += 1
        except IndexError:
            break
    print()  # new line after print
    return count
