#### User Defined Funcs are basically used for 2 reasons:
# 1) Code Re-use: defining a func, rather than writing 2-3 lines again & again after certain interval of time
# 2) Modularity : the concept of making multiple modules first and then linking and combining them to form a complete system 
#### (i.e, the extent to which a software/Web application may be divided into smaller modules is called modularity).

## NOTE: To use a func, there are 2 steps:
#### Step1) Defining a func
#### Step2) Calling a func

import os
os.system("cls")

def value_reverse(value):
    if type(value)==list or type(value)==str:
        reverse = value[::-1]
    else:
        temp = str(value)
        reverse = temp[::-1]
    return reverse
    # print(reverse)

#s="Python"
#result=value_reverse(s)
#print(result)

### Note: there are certain funcs that can return the value("str"), but there are alos some that cannot("append")

# l=[10,20,30,40]
# l.append(50)
# print(l)
# result2=value_reverse(l)
# print(result2)

num = 100
result = value_reverse(num)
print(result)


