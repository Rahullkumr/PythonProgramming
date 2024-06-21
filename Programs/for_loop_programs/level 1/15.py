# 15. 
# o/p ==> {0: 'Tomorrow', 1: 'is', 2: 'weekend', 3: 'and', 4: 'non-veg', 5: 'special'}

# s = 'tomorrow is weekend and non-veg special'
# d = dict()
# key = 0
# for word in s.split():
#     d[key] = word
#     key += 1

# print(d)

# sir's way
s = 'tomorrow is weekend and non-veg special'
d1 = dict()
word = s.split()
for i in range(0, len(word), 1):
    d1[i] = word[i]
print(d1)