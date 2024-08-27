
# x = 'good day wasted'
# for i in x:
#     if i == 'a':
#         break
#     print(i, end='')

# y = 'programming part in class'

# for i in y:
#     if i in 'aeiou':
#         continue
#     print(i, end="")
# print()

# reversed
# l = ['hello', 'hi', 'byebye']
# for i in l:
#     for j in reversed(i):
#         print(j, end='')
#     print()

# enumerate
# l = ['hello', 'hi', 'byebye']
# for i in enumerate(l):
#     print(i)

# zip

# l = ['hello', 'hi', 'byebye']
# l2 = [3,1,4,7]
# for i in zip(l,l2):
#     print(i)

# zip_longest

from itertools import zip_longest
l = ['hello', 'hi', 'byebye']
l2 = [3,1,4,7]
for i in zip_longest(l,l2):
    print(i)

