#!/usr/bin/python3
def uppercase(c):
    result = ''
    for i in c:
        if ord(i) >= 97 and ord(i) <= 122:
            result += chr(ord(i) - 32)
        else:
            result += i
    print(result, end=' \n')
