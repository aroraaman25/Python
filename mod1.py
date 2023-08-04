"""
Docstring: This is basic program of binary search
Author of this program is Devops Engineer

"""

# Note : A func that calls itself is known as a recursive function
## Q) Find out factorial of a number

# factorial(5)= 5 * fact(4)
#                    4 * fact(3)
#                          3 * fact(2)
#                                2 * fact(1)
#                                       1
import os
os.system("cls")

# def factorial(num):
#    if num == 1:
#       return 1
#    else:
#        return num * factorial(num - 1)

# num=5
# result=factorial(num)
# print(result)

## Q) Finding a value in list using binary search

def binary_search(l,key,low,high):
        if low>high:
                return -1
        else:
            mid = (low+high)//2
            if l[mid] == key:
                  return mid
               
            elif key < l[mid]:
                  return binary_search(l,key,low,mid-1)
            else:
                   return binary_search(l,key,mid+1,high)

# print(__name__)
if __name__ == '__main__':
      l = [100,200,300,400,500,600,700,800,900]
      key=900
      result=binary_search(l,key,0,len(l)-1)
      print(result)