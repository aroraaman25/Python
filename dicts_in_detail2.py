import os
os.system("cls")

# l1=[1,2,3,4,5]
# l2=[1,4,9,16,25]
# # print(d)

# l=[1,2,3,4,5]
#### to make the elements of the list as the keys for a new dictionary "dict.fromkeys" is used
# d = dict.fromkeys(l,0)  #### --- this "fromkeys" is a class method
# print(d)

#### Merging 2 dictionaries
d1={1:2,2:4,3:9,4:16}
# d2={5:25,6:36,7:49,8:64}
# d1.update(d2)
print(d1)

#### Deleting items from dictionary : pop, popitem, clear, del
# r = d1.pop(2)
# print(d1,r)

r = d1.popitem()
print(d1,r)

## NOTE: Diff b/w pop func & popitem func is that pop only returns the value, 
## whereas popitem also returns the deleted key along with the corresponding value

d1.clear() #### ---- this will clear all the elements in the dictionary
print(d1)