''' 
16.wap to create a dictionary words and its length pair

s="tomorrow is weekend and non-veg special"

o/p:-->{'tomorrow': 8, 'is': 2, 'weekend': 7, 'and': 3, 'non-veg': 7, 'special': 7}
'''


s = 'tomorrow is weekend and non-veg special'
d = {}
for i in s.split():
    d[i] = len(i)

print(d)