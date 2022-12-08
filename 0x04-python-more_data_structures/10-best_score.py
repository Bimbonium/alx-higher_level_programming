#!/usr/bin/python3
def best_score(a_dictionary):
    maxi = 0
    key_1 = ''
    if (a_dictionary):
        for k, v in a_dictionary.items():
            if v > maxi:
                maxi = v
                key_1 = k
        return key_1
