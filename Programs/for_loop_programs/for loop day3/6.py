# 6.wap to create a new list, of individual and collection data type from list

data=[20.12,True,[10,20],"super",{1,2},{"a":10},100,(8,9)]

indi = []
coll = []

for i in data:
    if isinstance(i, (int,float, complex, bool)):
        indi.append(i)
    else:
        coll.append(i)

print(indi)
print(coll)