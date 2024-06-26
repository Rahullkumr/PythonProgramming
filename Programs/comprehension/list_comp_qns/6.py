# 6.wap to create a list containing tuples having two elements that is index and value of list
l=["hey","hello","good","evening","python"]
# normal way
l2 = []
for i in enumerate(l):
    l2.append(i)
print(l2)

# list comp

print([i for i in enumerate(l)])