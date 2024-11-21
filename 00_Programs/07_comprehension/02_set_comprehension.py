'''Set Comprehension'''


# syntax1: v_n = {expression for loop condition}                            # without if and else condition
# syntax2: v_n = {expression for loop condition if condition}               # with if statement
# syntax3: v_n = {expression if condition else block for loop condition}    # with if-else statement


# 1. print square of elements in list
"""
x = [1,2,3,4,5,6]
square = {i**2 for i in x}
print(square)
"""

# 2. print only even nos in list
"""
x = [1,2,3,4,5,6]
even = {i for i in x if i % 2 == 0}
print(even)
"""

# 3. print even nos as it is and cube if it is odd
"""
x = [1,2,3,4,5,6]
z = {i if i%2 == 0 else i**3 for i in x}
print(z)
"""