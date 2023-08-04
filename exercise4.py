# WAP to calculate the sum & average of n integer numbers

import os
os.system("cls")

# l=[0,1,2,3,4,.......n]
def sum(n):
    add=0
    for value in range(1,n+1):
        add=add+value
        print(add)
    return add
n=6
SUM=sum(n)
print(SUM)

avg=SUM/n
print(avg)