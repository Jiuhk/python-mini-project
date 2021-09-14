from math import *


def power(num):
    a = pow(num, 3)
    return sqrt(a)


result = power(4)
print(result)


def printer(wd):
    print(wd)


printer("hi")


def power_up(num):
    num*num


var = input("Enter a number: ")
power_up(int(var))
print(var)
