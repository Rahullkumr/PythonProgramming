'''
4.wap to replace all the character with "-"
if the characters occurs more than once in a string
o/p:
-e--o-ai
'''

s = "hellohai"
# count = 1
print(s.count('h'))

for ch in s:
    if s.count(ch) > 1:
        print("-", end="")
    else:
        print(ch, end="")
