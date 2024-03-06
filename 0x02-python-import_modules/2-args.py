#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    num = len(argv) - 1

    if num == 1:
        print("{:d} argument".format(num))
    else:
        print("{:d} arguments".format(num))
    for i in range(1, len(argv)):
        print("{:d}: {}".format(i, argv[i]))
