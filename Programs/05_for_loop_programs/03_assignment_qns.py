'''For loop Assignment qns'''


# 1.wap to Sum the numbers
"""
s = 'Sony12India567pvt21ltd'
sum = 0
n = ''
for i in s:
    if i.isnumeric():
        sum += int(i)
print(f'Sum of digits is: {sum}')
"""
# ===========================================================

# 2.Print all the missing numbers from 1-10 in the below list
"""
l = [1, 2, 3, 4, 6, 7, 10]
for i in range(1, 11):
    if i not in l:
        print(i)
"""
# ===========================================================

# 3.WAP to remove duplicates from the list without using inbuilt function
"""
d = [1,2,3,4,5,6,7,1,2,3,4]
# print(set(d))
dup = []
non_dup = []
for i in d:
    if i not in non_dup:
        non_dup.append(i)
    else:
        dup.append(i)
print(dup) # [1, 2, 3, 4]
print(non_dup) # [1, 2, 3, 4, 5, 6, 7]
"""
# ===========================================================

# 4.wap to replace all the character with "-"
# if the characters occurs more than once in a string
# o/p: -e--o-ai

# my way
"""
s = "hellohai"
for ch in s:
    if s.count(ch) > 1:
        print("-", end="")
    else:
        print(ch, end="")
"""

# sir's way
"""
s = "hellohai"
for i in s:
    if s.count(i) > 1:
        s = s.replace(i, '-')
print(s)
"""
# ===========================================================

# 5. WAP to print all numeric values in a list
"""
l = ['apple', 123, 'google', '45.6','yahoo', [1,2,3],True, (1,3,7), 6+3j]
for element in l:
    if isinstance(element, (int, float, complex, bool)):
        print(element)
"""
