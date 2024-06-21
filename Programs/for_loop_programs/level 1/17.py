'''
17.wap to create a dictionary characters and its corresponding upper case characters
s="sunday"
o/p:-->{'s': 'S', 'u': 'U', 'n': 'N', 'd': 'D', 'a': 'A', 'y': 'Y'}
'''
s="sunday"
d = dict()

# using built-in method
# for i in s:
#     d[i] = i.upper()
# print(d)

# without using inbuilt method

for i in s:
    d[i] = chr(ord(i) - 32)
print(d)