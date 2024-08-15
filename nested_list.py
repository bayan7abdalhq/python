nested_list = [1,[1,2,3], 4, 5]

# my_list = [1, 1 ,2 ,3, 4, 5]
my_list = []

for item in nested_list:
    # item = 1
    # item=[1,2,3]
    if isinstance(item, list):
        for inner_item in item:
            my_list.append(inner_item)
    else:
        my_list.append(item)

print(my_list)


