# Note: there are set of meta-characters used in regular expressions

## Below mentioned regular expressions are for matching only a single char at a time
### '.' ----- it will match with any char, i.e. digit/special-char/alphabaets except new line
### '[a-z]' ---- it will match alphabets and for that we can specify the range. It is known as char-class.
### '[0-9]' ---- digit-class, it will match digits

## Below mentioned expresssions are for matching multiple char at a time
### '+' ----- this means atleast one
### '*' ----- this means zero or more

## Other used Regular Expressions
### '^' ----- used to match something at the start of the string
### '$' ----- used to match something at the end of the string
### '?' ----- used to specify something that is optional
### '[a-z]{2,4}' ----- this means it is expecting atleast 2 char and atmost 4 char in the specified alphabetical range

# Q) To validate whether a PAN number is a valid PAN number or not.
import os
os.system("cls")

import re
PAN="ABCDE1234A"
r=re.compile("^[A-Z]{5}[0-9]{4}[A-Z]$")
output=re.findall(r,PAN)
print(output)

# Q) To check whether a phone number is a valid phone number or not, 1st digit cannot be 0 & it has to be between 6-9
num="7876556789"
r = re.compile("^[6-9][0-9]{9}$")
result=re.findall(r,num)
print(result)

# Q) To check whether the given date is valid or not. Pattern: dd-mm-yyyy
date="23-12-1997"
r= re.compile("^[0-9]{2}-[0-9]{2}-[0-9]{4}")
answer=re.findall(r,date)
print(answer)

