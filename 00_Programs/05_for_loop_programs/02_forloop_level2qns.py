'''For loop level 2'''


# 15.wap to create a dictionary index and word pair
# s="tomorrow is weekend and non-veg special"
# o/p ==> {0: 'Tomorrow', 1: 'is', 2: 'weekend', 3: 'and', 4: 'non-veg', 5: 'special'}

# my way
"""
s = 'tomorrow is weekend and non-veg special'
d = dict()
key = 0
for word in s.split():
    d[key] = word
    key += 1
print(d)
"""

# sir's way
"""
s = 'tomorrow is weekend and non-veg special'
d1 = dict()
word = s.split()
for i in range(0, len(word), 1):
    d1[i] = word[i] 
print(d1)
"""
# =================================================

# 16.wap to create a dictionary words and its length pair
# s="tomorrow is weekend and non-veg special"
# o/p:-->{'tomorrow': 8, 'is': 2, 'weekend': 7, 'and': 3, 'non-veg': 7, 'special': 7}
"""
s = 'tomorrow is weekend and non-veg special'
d = {}
for i in s.split():
    d[i] = len(i)

print(d)
"""
# =================================================

# 17.wap to create a dictionary characters and its corresponding upper case characters
# s="sunday"
# o/p:-->{'s': 'S', 'u': 'U', 'n': 'N', 'd': 'D', 'a': 'A', 'y': 'Y'}
"""
# using built-in method
s="sunday"
d = dict()
for i in s:
    d[i] = i.upper()
print(d)

# without using inbuilt method
s="sunday"
d = dict()
for i in s:
    d[i] = chr(ord(i) - 32)
print(d)
"""
# =================================================

# 18.wap to create a dictionary Ascii and character pair
# o/p:--> {89: 'Y', 51: '3', 111: 'o', 77: 'M', 108: 'l', 120: 'x'}
"""
l=[89,51,111,77,108,120]
d = {}

for i in l:
    d[i] = chr(i)
print(d)
"""
# =================================================

# 19.wap to  create a list of characters and its Ascii value pair
# o/p:-->[('s', 115), ('u', 117), ('n', 110), ('d', 100), ('a', 97), ('y', 121)]
"""
s="sunday"
l = []
for ch in s:
    l.append((ch, ord(ch)))
print(l)
"""
# =================================================

# 20.WAp to perform clear() in list without using inbuilt method
"""
lst= ['hai', 'hello', 'python', 'world', 'jingalala']
lst = []
print(lst)
"""
# =================================================

# 21. wap to create a dictionary with words and its length pair and ends with vowel
"""
s="Today is Tuesday and attending python session"
d = dict()
for i in s.split():
    if i.endswith(('a', 'e', 'i', 'o', 'u')):
        d[i] = len(i)
print(d)
"""
# =================================================

# 22.wap to create a dictionary with letter and its words starting with that letter pair
# s = "hi hello good morning welcome to python session"
# o/p:-->{'h': ['hi', 'hello'], 'g': ['good'], 'm': ['morning'], 'w': ['welcome'], 't': ['to'], 'p': ['python'], 's': ['session']}

# my way
"""
s = "hi hello good morning welcome to python session"
dow = {}
words = s.split()
temp_list = []

for i in words:
    temp_list = []
    first_char = i[0]
    for w in words:
        if w.startswith(first_char):
            temp_list.append(w)
    dow[first_char] = temp_list
print(dow)
"""

# sir's way
"""
s = "hi hello good morning welcome to python session"
d = {}
for i in s.split():
    if i[0] not in d:
        d[i[0]] = [i]
    else:
        d[i[0]] += [i]
print(d)
"""
# =================================================


# 23.wap to create a dictionary of characters and its indices pair
# s="hello python"
# o/p:-->{"h":[0,9],"e":1..........}
"""
s="hello python"
d = {}
for i in s:
    d[i] = s.index(i)
print(d)

if i not in d:
    d[i] = [s.index(i)]
else:
    d[i[0]] += [i]
"""
# =================================================

# 24.wap to create a dictionary word and reverse word pair
# s="tomorrow is weekend and non-veg special"
# o/p:-->{'tomorrow': 'worromot', 'is': 'si', 'weekend': 'dnekeew', 'and': 'dna', 'non-veg': 'gev-non', 'special': 'laiceps'}
"""

"""
# =================================================

# 25.Reverse a list without using any built-in functions and slicing.
# l = [1, 2, 3, 4]
"""

"""