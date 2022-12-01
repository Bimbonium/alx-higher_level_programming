#!/usr/bin/python3
if __name__ == "__main__":

    from sys import argv as argvector
    arg_len = len(argvector)
    counter = 1  # to count from 1 to arg_len
    if arg_len == 0:
        print('{} arguments.'.format(len(argvector)))
    elif arg_len == 1:
        print('{} argument:'.format(len(argvector)))
        print('{}: {}'.format(arg_len, argvector[arg_len - 1]))
    else:
        print('{} arguments:'.format(len(argvector)))
        for i in argvector:
            while counter != arg_len + 1:
                print('{}: {}'.format(counter, argvector[counter - 1]))
                counter += 1
