#!/usr/bin/python3
import sys
if __name__ == "__main__":
    num = len(sys.argv)
    if num == 2:
        print("1 argument:")
        print("1: {}".format(sys.argv[1]))
    elif num > 2:
        print("{} arguments".format(num - 1))
        for i in range(1, num):
            print("{}: {}".format(i, sys.argv[i]))
    else:
        print("no arguments:")
