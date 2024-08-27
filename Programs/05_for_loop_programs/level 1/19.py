'''
19.wap to  create a list of characters and its Ascii value pair
o/p:-->[('s', 115), ('u', 117), ('n', 110), ('d', 100), ('a', 97), ('y', 121)]
'''
s="sunday"

l = []
for ch in s:
    l.append((ch, ord(ch)))
print(l)