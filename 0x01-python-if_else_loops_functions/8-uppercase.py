#!/usr/bin/python3
def uppercase(str):
    case_definer = 0
    for i in str:
        if ord(i) >= 97 and ord(i) <= 122:
            case_definer = 32
        else:
            case_definer = 0
        print('{}'.format(chr(ord(i) - case_definer)), end='')
    print('')
