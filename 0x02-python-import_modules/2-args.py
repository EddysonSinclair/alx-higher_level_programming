#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    num = len(argv)
    if num == 2:
        print("{:d} argument".format(num - 1))
        for i in range(1, num):
            print("{:d}: {}".format(i, argv[i]))
    elif num > 2:
        print("{:d} arguments".format(num - 1))
        for i in range(1, num):
            print("{:d}: {}".format(i, argv[i]))
    else:
        print("{:d} arguments".format(num - 1))
