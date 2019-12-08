from module01 import *

a=int(input("Enter 1st number: "))
b=int(input("Enter 2nd number: "))

print(mul(a,b))
print(add(a,b))
print(div(a,b))
print(sub(a,b))

from math import *

print(factorial(6))
print(sin(0))

list1 = [int(x) for x in input("enter number seperated by space : ").split(" ")]
print(list1)