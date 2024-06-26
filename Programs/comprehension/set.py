# Set comprehension

# 1. 
x = [1,2,3,4,5,6]
# # print square of elements in list
# # normal way

# # mentos way
# square = {i**2 for i in x}
# print(square)

# # 2. print only even nos in list
# x = [1,2,3,4,5,6]
# # normal way

# # mentos way
# even = {i for i in x if i % 2 == 0}
# print(even)

# 3. print even nos as it is and cube if it is odd
x = [1,2,3,4,5,6]
# normal way

# mentos way
z = {i if i%2 == 0 else i**3 for i in x}
print(z)