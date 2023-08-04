# Dictionaries are also called as Hash Maps
# In Dics, the elements are stored in Key-Value Pairs
# Dictionaries are Un-Ordered Data-Structure, so it does not support indexing and slicing
# Dictionary is a Mutable Data-Type just like "List" & "Tuple"
# keys should be unique i.e. for one key their should be a unique value
# keys should be immutable: i.e. only int, float, tuple & str data-structures are allowed

# Note: As soon as we create a dict, python in the background creates a Hash Table, 
# due to which the output of the dict is faster as compared to other Data-types

import os
os.system("cls")

d={"emp_name":"aman","emp_id":"a2023","emp_gender":"Male"}
# print(d,id(d))
# d["contact_number"]="1234554321"      ## --- this will update the dict with the contact number
# print(d,id(d))
# d["contact_number"]="54321012345"     ## --- this 2nd time same addition will work as update operation
# print(d,id(d))

# print(d["emp_id"])

# get func & setdefault func:
# print(d.get("emp_name"),d.get("emp_id"),d.get("age","Key does not exist"),d.get("emp_gender","Key does not exist"))
# print(d.setdefault("age",26))
# print(d)

################## Note: 
# the diff b/w get func & setdefault func is that get func only checks whether the key is present in the dict or not whereas 
# setdefault func adds that key to the dict with "None" as the default value


### Note: Iterating over a Dict only gives Keys as the output
# for x in d:
#    print(x)
# for key in d:
#    print(key,d[key])

# d={}
# for value in range(1,11):
#    d[value]=value*value
# print(d)

######### keys, values & items function in dict:
print(d.keys())      ###### ------ this will print all the keys present in the dictionary
print(d.values())    ###### ------ this will print all the values in the dictionary
print(d.items())     ###### ------ this will print all the elements in the dic