import random

list1=[]
list2=list()
for i in range (3):
    throw=random.randint(1,100)
    while throw in list1:
        throw=random.randint(1,100)
    list1.append(throw)
for j in range (3):
    throw=random.randint(1,100)
    while throw in list2 or throw in list1:
        throw=random.randint(1,100)
    list2.append(throw)
max_list1=0
max_list2=0
for j in range(j,3):
    if  list1[j]>=max_list1:
        max_list1=list1[j]
    if list2[j]>=max_list2:
        max_list2=list2[j]
if max_list1>max_list2:
     print("list1 kazandi")
else:
     print("mahmut kazandi")
