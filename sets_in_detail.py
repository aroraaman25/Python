# Rules:
# 1) Sets are mutable just like list & dict : there are methods to add, update & delete the elements
# 2) Sets are un-ordered i.e. does not follow indexing and slicing
# 3) All the elements in the set should be unique
# 4) Only im-mutable elements can be added in the sets

import os
os.system("cls")

# s={10,20,30,40}
# print(s,type(s))
# s.add(100)
# print(s)

s1={10,20,30,40,50,60}
s2={40,50,60,70,80,90}

#### NOTE: below are those operations in which the func. woks on the original set and the o/p is stored in a new set
# s3=s1.union(s2)
# print(s3)

# s4=s1.intersection(s2)
# print(s4)

# s5=s1.difference(s2)    ### --- this will print those elements that are present in s1 but not in S2 
# print(s5)

# s6=s1.symmetric_difference(s2)    #### ----- this gives the output as all the elements in s1 & s2 except the common elements
# print(s6)

#### NOTE: below are those operations in which the func. woks on the original set and the o/p is reflected in the original set itself

# s1.update(s2)
# print(s1)

# s1.intersection_update(s2)
# print(s1)

# s1.difference_update(s2)
# print(s1)
# s2.difference_update(s1)
# print(s2)

s1.symmetric_difference_update(s2)
print(s1)

