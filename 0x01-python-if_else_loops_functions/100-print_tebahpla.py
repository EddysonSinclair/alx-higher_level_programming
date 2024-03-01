#!/usr/bin/python3
count = 1;
for i in range(122, 96, -1):
    if count % 2 == 0:
        print("{}".format(chr(i - 32)), end="")
        count += 1
    else:
        print("{}".format(chr(i)), end="")
        count += 1
