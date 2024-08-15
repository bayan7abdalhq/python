#Python Program to Remove Duplicate Element From a List
list1 =[1 , 1 ,2 ,3 ,4 ,4,5,5 ,6]

list2 = []

for item in list1:
    if item not in list2:
       list2.append(item)

print(list2)
