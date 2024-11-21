# present in for loop file page: 7

# zip

l = ['hello', 'hi', 'byebye']
l2 = [3,1,4,7]
for i in zip(l,l2):
    print(i)

# zip_longest

from itertools import zip_longest
l = ['hello', 'hi', 'byebye']
l2 = [3,1,4,7]
for i in zip_longest(l,l2):
    print(i)