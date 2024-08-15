#list
my_list=[1,2,3,4,5]
#add to list
my_list.append(6)
print(my_list)

#remove from list
my_list.pop(0)#remove from specific position
my_list.remove(2)#remove from specific value
print(my_list)

#modify list
my_list[1:2] =[7,8]
print(my_list)
my_list.insert(2, 9)
print(my_list)

#dict
my_dict = {
    "name":"jana",
     "age":17,
    "id":"34"
}
#add to dict
my_dict["color"] = "red"
print(my_dict)

#remove from dict
my_dict.pop("age")
print(my_dict)

my_dict.popitem()
print(my_dict)

del my_dict["id"]
#modify dict
my_dict.update({"color": "green"})
print(my_dict)


#tuple
my_tuple = ("apple", "banana", "cherry", "apple", "cherry")
#add to tuple
y = list(my_tuple)
y.append("orange")
my_tuple = tuple(y)
print(my_tuple)

#remove from tuple
y.remove("apple")
my_tuple = tuple(y)
print(my_tuple)

#modify tuple
y[1] = "kiwi"
my_tuple = tuple(y)
print(my_tuple)