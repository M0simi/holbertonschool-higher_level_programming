#!/usr/bin/python3

def search_replace(my_list, search, replace):
    new_list = []
    for item in my_list:
        if item == search:
            new_list.append(replace)
        else:
            new_list.append(item)
    return new_list

# def search_replace(my_list, search, replace):
    #return list(map(lambda x: replace if x == search else x, my_list))

# list comperhension
# def search_replace(my_list, search, replace):
    #return [replace if x == search else x for x in my_list]
