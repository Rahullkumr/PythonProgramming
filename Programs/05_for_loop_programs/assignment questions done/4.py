'''
4.wap to replace all the character with "-"
if the characters occurs more than once in a string
o/p:
-e--o-ai
'''

s = "hellohai"

# for ch in s:
#     if s.count(ch) > 1:
#         print("-", end="")
#     else:
#         print(ch, end="")


# sir's way

for i in s:
    if s.count(i) > 1:
        s = s.replace(i, '-')

print(s)