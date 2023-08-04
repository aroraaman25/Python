# WAP to print the factorial of a number

import os
os.system("cls")

def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num-1)

result=factorial(5)
print(result)