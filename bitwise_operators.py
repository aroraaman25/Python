# there are 6 bitwise operators in coding language: &, |, ^, ~, <<, >>

import os 
os.system("cls")

# & operator: we will only see 1 of both bits are 1
num1=1
num2=0
#print(num1 & num2)

# | operator: we will see 1 if atleast one of them is 1
#print(num1 | num2)

# ^ operator: also known as exclusive OR: if one of them is 0, result is 0 and if both are 0, result will be 0
#print(num1 ^ num2)

# ~ operator: also known as logical negation
#print(~0)

# << operator: left shift operator: means multiply by the given number
print (12 << 1)

# >> operator: right shift operator: divide by the given number
print(12 >> 2)