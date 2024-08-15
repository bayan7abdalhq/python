items =[0,1]
#items = 0 ,1 ,1
n=5
for i in range(2,n):
    result = items[i-2] + items[i-1]
    items.append(result)
print(items)




