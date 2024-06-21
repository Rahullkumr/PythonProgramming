# 18.wap to create a dictionary Ascii and character pair

# o/p:-->{89: 'Y', 51: '3', 111: 'o', 77: 'M', 108: 'l', 120: 'x'}


l=[89,51,111,77,108,120]
d = {}

for i in l:
    d[i] = chr(i)
print(d)