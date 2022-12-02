#!/usr/bin/python3
if __name__ == "__main__":

    from sys import argv as argvector
    arg_len = len(argvector)
    counter = 1  # to count from 1 to arg_len
    if arg_len == 1:
        print('{} arguments.'.format(arg_len - 1))
    elif arg_len == 2:
        print('{} argument:'.format(arg_len - 1))
        print('{}: {}'.format(arg_len - 1, argvector[arg_len - 1]))
    else:
        print('{} arguments:'.format(arg_len - 1))
        for i in argvector:
            while counter != arg_len:
                print('{}: {}'.format(counter, argvector[counter]))
                counter += 1
