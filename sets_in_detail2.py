import os
os.system("cls")

# s1={100,200,300,400,500}
# print(s2.issubset(s1))  ### --- to check whether all the elements of s2 are present in s1 or not

# print(s1.issuperset(s2)) ### --- this checks that elements that are present in s2 are already there in s1

# l = [10,20,30,40,50]
# s = set(l)
# print(s)

## Q: If we have 2 lists, we have to make a single sorted list with unique elements in it

l1=[10,20,30,100,200,300]
l2=[400,800,1200,1600,2000,80,100,120,160]
s1=set(l1)
s2=set(l2)
s3=s1.union(s2)
l0=list(s3)
l0.sort()
print(l0)

## Delete operations in set data-type : pop, remove, discard, clear, del

s={100,200,300,400,500,600}
# r=s.pop()
# print(s,r)

# r1=s.remove(200)
# print(s)

s.clear()
print(s)
