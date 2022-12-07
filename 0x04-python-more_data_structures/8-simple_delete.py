#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    dictionary2 = {}
    for k, v in a_dictionary.items():
        if k == key:
            continue
        else:
            dictionary2[k] = v
    return dictionary2
