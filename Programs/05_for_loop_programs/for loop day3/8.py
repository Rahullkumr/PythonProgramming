# 8.wap to create a dictionary characters and its count pair

char=["a","M","i","A","M","I","i","H","a","H"]
dc = {}
for i in char:
    dc[i] = char.count(i)

print(dc)