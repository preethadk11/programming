data=[1,2,3,2,4,1,5]
duplicate=[x for x in set(data) if data.count(x)>1]
print(duplicate)