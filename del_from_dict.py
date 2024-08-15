# Python Program to Delete an Element From a Dictionary if it exist
my_dict = {'a': 1, 'b': 2, 'c': 3}
def remove_key(my_dict, key):
    if key in my_dict:
        del my_dict[key]


remove_key(my_dict, 'b')
print("Updated dictionary:", my_dict)