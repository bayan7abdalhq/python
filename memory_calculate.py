list=[1,2,3]
print(id(list))

list2=[4,5,6,7]
print(id(list2))

difference = abs(id(list) - id(list2))
print(difference)