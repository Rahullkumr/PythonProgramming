# Dictionary 07_comprehension

# syntax1: v_n = {key:value for loop condition} # without if and else condition
# syntax2: v_n = {key:value for loop condition if condition} # with if statement
# syntax3: v_n = {key:value if condition FSB for loop condition} # with if-else statement

# 1.
s = '07_comprehension'
# o/p: {'c': 99, 'o': 111, 'm': 109, 'p': 112, 'r': 114, 'e': 101, 'h': 104, 'n': 110, 's': 115, 'i': 105}
# # normal
# d = {}
# for i in s:
#     # key=value
#     d[i] = ord(i)
# print(d)

# # using dictionary 07_comprehension
# d = {i:ord(i) for i in s}
# print(d)

# 2.
y = [11,12,13,14,15]
# print square of odd numbers and keep the even as it is using dict comp
# o/p: {11: 121, 12: 12, 13: 169, 14: 14, 15: 225}
# normal

# dict comp
print({i:i**2 if i%2 == 1 else i for i in y})
