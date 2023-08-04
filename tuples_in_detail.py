# tuple: immutable data-structure, also ordered so it offers slicing and indexing 
# tuples are widely used in python especially to pass values from one func. to another func.

import os
os.system("cls")

# t=(10,20,20,20,30,30,40)
# print(t, type(t))
# print(t[-2]) #### -------- indexing
# print(t[:2]) #### -------- slicing

## Note: there are only 2 built-in methods for Tuple i.e. count & index
# print(t.index(30))
# print(t.count(20))

### Use of enumerate

l=[10,20,30,40,50]
#for (index,value) in enumerate(l):
#    print(index,value)
######## OR #########
# for t in enumerate(l):
#   print(t)

### To convert List into Tuple
t=tuple(l)     ########## converts a list into tuple
print(t)

t=(10,20,30,40)
l=list(t)      ########## converts tuple into a list
print(l)
