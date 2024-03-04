#!/usr/bin/python3
import sys
if __name__ == "__main__":
    num = len(sys.argv)
    if num == 0:
        print("no argument.")
    else:
        print("{} arguments:".format(num - 1))
        for i in range(num):
            if i == 0:
                continue
            print("{}: {}".format(i, sys.argv[i]))
