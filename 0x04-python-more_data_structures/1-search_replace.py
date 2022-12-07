#!/usr/bin/python3
def search_replace(my_list, search, replace):
    my_list_1 = []
    for index, value in enumerate(my_list):
        if value == search:
            my_list_1.append(replace)
        else:
            my_list_1.append(my_list[index])
    return my_list_1
