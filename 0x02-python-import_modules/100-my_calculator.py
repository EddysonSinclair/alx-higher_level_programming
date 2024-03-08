#!/usr/bin/python3

from sys import argv
from calculator_1 import add, sub, mul, div
if __name__ == "__main__":
    num = len(argv) - 1
    if num != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        for i in range(0, num, 3):
            a = int(argv[i * 2 + 1 ])
            b = int(argv[i * 2 + 3])
            if argv[i * 2 + 2] == '+':
                print('{} + {} = {}'.format(a, b, add(a, b)))
            elif argv[i * 2 + 2] == '-':
                print('{} - {} = {}'.format(a, b, sub(a, b)))
            elif argv[i * 2 + 2] == '*':
                print('{} * {} = {}'.format(a, b, mul(a, b)))
            elif argv[i * 2 + 2] == '/':
                print('{} / {} = {}'.format(a, b, div(a, b)))
            else:
                print("Unknown operator. Available operators: +, -, * and /")
                exit(1)
