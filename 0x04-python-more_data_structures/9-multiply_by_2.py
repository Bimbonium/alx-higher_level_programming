#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    dictionary_2 = {}
    for k, v in a_dictionary.items():
        dictionary_2[k] = v * 2
    return dictionary_2
