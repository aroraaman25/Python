## Some Built-in funcs python provides from mathematical operations
import os
os.system("cls")

# Q1) Sum of all elements in a list
# l=[10,20,30,40,50]
# print(sum(l))
# print(max(l))   ## -- this will print the largest value element in the list
# print(min(l))

# Q2) Round off the decimal number
# num=25.556
# print(round(num))

#### Math Module

import math

####  1st:
# l=[0.1] * 10
# print(l)
# print(sum(l))
# print(math.fsum(l))

#### 2nd:
# num1=15.5559
# print(math.factorial(5))

#### 5th:
# num1=15.5554
# print(math.modf(num1))
# d, i = math.modf(num1)
# print(d), print(i)

#### 6th:
# print(math.pow(5,2))

#### 7th:
# print(math.log(10,2))
# print(math.log10(2))


#### RANDOM Module

import random

print(random.random())

l=[1,2,3,4,5,6]
print(random.choice(l))

print(random.randint(1,5))
print(random.randrange(1,5))   ##### in this the last value i.e. in this case 5 is exclusive from the operation