#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv

if __name__ == "__main__":
    ac = len(argv)
    if ac != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    funcs= {"+": add, "-": sub, "*": mul, "/": div}
    o = argv[2]
    if o not in funcs:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    a = int(argv[1])
    b = int (argv[3])
    print("{:d} {:s} {:d} ={:d}".format(a, o, b, funcs[o](a, b)))
