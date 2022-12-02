#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv as argvec
    add_ = 0
    counter = 1
    while counter != len(argvec):
        add_ += int(argvec[counter])
        counter += 1
    print('{}'.format(add_))
