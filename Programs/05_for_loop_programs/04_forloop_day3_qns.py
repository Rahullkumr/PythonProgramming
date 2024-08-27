'''For loop Day 3 qns'''


# 1.wap to print first and last char of each name in the list
"""
a = ["Sunil","anil","Suresh","Mahesh","Dinesh"]
for w in a:
    print(w[0], w[-1])
"""
# =====================================================================

# 2.wap to create a new list as square of each number of below list
"""
b=[2,4,5,6,7,1]
square = []
for i in b:
    square.append(i**2)
print(square)
"""
# =====================================================================

# 3.wap if number is even then print its square else print its cube
"""
c=[2,4,5,3,7,9]
l = []
for i in c:
    if i % 2 == 0:
        l.append(i**2)
    else:
        l.append(i**3)

print(l)
"""
# =====================================================================

# 4.wap to create a list with square and cube of each numbers
"""
d=[2,4,5,1,8,9,10]
# o/p-->[(4, 8), (16, 64), (25, 125), (1, 1), (64, 512), (81, 729), (100, 1000)]
l = []
for i in d:
    l.append((i**2, i**3))
print(l)
"""
# =====================================================================

# 5.wap to create a new list of reversing each name from the list
"""
names=["prince","Rekha","Madhu","Sindhu","denga","manga"]
rev_names = []
for i in names:
    rev_names.append(i[::-1])
print(rev_names)
"""
# =====================================================================

# 6.wap to create a new list, of individual and collection data type from list
"""
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
"""
# =====================================================================

# 7.wap to print author name in books dictionary
"""
books={"love story":["Harish",30],"biography":["padam",150],"animals":["vimala",75]}

for i in books.values():
    print(i[0])
"""
# =====================================================================

# 8.wap to create a dictionary characters and its count pair
"""
char=["a","M","i","A","M","I","i","H","a","H"]
dc = {}
for i in char:
    dc[i] = char.count(i)

print(dc)
"""
# =====================================================================

# 9.wap to group fruit name and country pair
"""
d={"apple":45,"mango":67,"cherry":90,"berry":23}
p={"India":"Kashmir","America":"us","UK":"Toronto","Africa":"Uganda"}
for i in zip(d,p):
    print(i)
"""
# =====================================================================

# 10.wap to group fruit name and country pair only if a fruit is even length
"""
from itertools import zip_longest
d={"apple":45,"mango":67,"cherry":90,"berry":23}

p={"India":"Kashmir","America":"us","UK":"Toronto","Africa":"Uganda"}

for i in zip(d,p):
    if len(i[0]) % 2 == 0:
        print(i)
"""
# =====================================================================

# 11.wap to sum of same index element from l1,l2,l3
"""
l1=[10,20,30,40]
l2=[78,44,11,99]
l3=[1,2,3,4]
for i in zip(l1,l2,l3):
    print(sum(i))
"""
# =====================================================================

# 12.wap to pair values of both dictionary
"""
d={"apple":45,"mango":67,"cherry":90,"berry":23}
p={"Kashmir":"india","America":"us","UK":"Toronto","Africa":"Uganda"}
for i in zip(d.values(), p.values()):
    print(i)
"""
# =====================================================================

# 13.WAP to print sum of internal and external list
# l = [[1,2,3], [4,5,6], [7,8,9]]
# output:
   #internal = 6, 15, 24
   #external --> 45

# my way
'''
l = [[1,2,3], [4,5,6], [7,8,9]]
internal = []
for i in l:
   internal.append(sum(i))
external = sum(internal)
print(*internal) # * for removing square bracket i.e []
print(external)
'''
# sir's way
"""
l = [[1,2,3], [4,5,6], [7,8,9]]
res = []
for i in l:
   sum_internal = 0
   for j in i:
      sum_internal += j
   res.append(sum_internal)
print(res);
"""
# =====================================================================

# 14.wap using below list and get the below output
# l = ['sun flower', 'Lilly flower', 'Marigold flower', 'lion animal', 'tiger animal', 'eagle bird', 'snake animal', 'lotus flower', 'pigeon bird']
# o/p:-->{'flower': ['sun', 'Lilly', 'Marigold', 'lotus'], 'animal': ['lion', 'tiger', 'snake'], 'bird': ['eagle', 'pigeon']}

# my way
"""
l = ['sun flower', 'Lilly flower', 'Marigold flower', 'lion animal', 'tiger animal', 'eagle bird', 'snake animal', 'lotus flower', 'pigeon bird']
d = {}
category_list = []
for i in l:
  category = i.split()[1] 
  if category not in d.keys():
    for j in l:
      if j.split()[1] ==  category:
        if j.split()[0] not in category_list:
          category_list.append(j.split()[0])
    d[category] = category_list
    category_list = []
print(d)
"""

# Vaibhav's way
"""
l = ['sun flower', 'Lilly flower', 'Marigold flower', 'lion animal', 'tiger animal', 'eagle bird', 'snake animal', 'lotus flower', 'pigeon bird']
categories = {}
for item in l:
  words = item.split()
  category = words[-1]
  word = ' '.join(words[:-1])
  categories.setdefault(category, []).append(word)
print(categories)
"""

# Sir's code
"""
l = ['sun flower', 'Lilly flower', 'Marigold flower', 'lion animal', 'tiger animal', 'eagle bird', 'snake animal', 'lotus flower', 'pigeon bird']
d = {}
for i in l:
    x = i.split()
    if x[1] not in d:
        d[x[1]] = [x[0]]
    else:
        d[x[1]] += [x[0]]
print(d)
"""