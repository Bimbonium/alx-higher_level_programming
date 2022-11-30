#!/usr/bin/python3
def remove_char_at(str, n):
    if n >= 0 and n < len(str):
        a = n + 1
        str1 = str[:n] + str[a:]
        return str1
    else:
        return str
