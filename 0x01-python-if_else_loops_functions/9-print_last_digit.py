#!/usr/bin/python3
def print_last_digit(number):
    if number > 0:
        a = number % 10
    elif number < 0:
        a = number % -10
    else:
        a = 0
    print(f'{a}')
    return a
