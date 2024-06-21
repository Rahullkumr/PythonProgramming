'''
23.wap to create a dictionary of characters and its indices pair

s="hello python"

o/p:-->{"h":[0,9],"e":1..........}
'''
s="hello python"
d = {}

for i in s:
    d[i] = s.index(i)

print(d)

# if i not in d:
#         d[i] = [s.index(i)]
#     else:
#         d[i[0]] += [i]