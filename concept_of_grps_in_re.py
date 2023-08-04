import os 
os.system("cls")

import re

# Q) To check whether the given date is valid or not. Pattern: dd-mm-yyyy

# date="23-12-1997"
# r= re.compile("^[0-9]{2}-[0-9]{2}-[0-9]{4}$")
# result=re.search(r,date)
# if result:
  #  print(result.group())
# else:
  #  print("Pattern not matched")

# Note: print(result) will give the match objects, but if we want the value of the match objects, then we have to use group func as used above

# Note: the main dif b/w search pattern and findall pattern is that in findall, it will search all the occurences, wheras search pattern will search only for the 1st occurence,
##      so if the 1st occurence matches the pattern it will return the match object, else will return none.


## Extracting Data from a matched string by using 'groups' concept

date="23-12-1997"
r= re.compile("^([0-9]{2})-([0-9]{2})-([0-9]{4})$")
result=re.search(r,date)
if result:
    print(result.group(3))
else:
    print("Pattern not matched")

## ********** OR **********

date="23-12-1997"
r= re.compile("^(?P<date>[0-9]{2})-(?P<month>[0-9]{2})-(?P<Year>[0-9]{4})$")
result=re.search(r,date)
if result:
    print(result.group("month"))
else:
    print("Pattern not matched")


### Example of a number with or without +91

num="+91 7876556789"
r = re.compile("^(\+91\s)?[6-9][0-9]{9}$")
result=re.search(r,num)
print(result.group())


