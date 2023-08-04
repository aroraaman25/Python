# update : to update any element in the list
import os
os.system("cls")
l = [10,20,30,40,50]
#print(l)
#l[2]=500 ###-------30 got updated to 500
#print(l)

# Delete: to delete elements we have diff. funcs: pop, remove, clear & del
#Pop: 
#r=l.pop(1) ###-------- automatically removes the last element from the list
#print(l,r)

#Remove: to remove the elements on the basis of values, remove func is used
l.remove(30)
#print(l)

#Clear: to clear all the elements from the list
l.clear()
#print(l)

#Del: to remove the list completely from the memory location, we can use Del func
del l



