'''List comprehension assignment'''


# 1.wap to check even numbers in a list and return a list containing only even numbers
"""
l=[2,32,1,52,31,24,56,75]
even = [i for i in l if i % 2 == 0]
print(even)
"""

# 2.wap to check elements inside the collection are even or odd,if it is even make it square of that numbers,if it is odd make it as cube of that numbers
"""
l=[2,3,5,1,7,2,3]
res = [i**2 if i%2==0 else i**3 for i in l]
print(res)
"""

# 3.wap to return a list containing 10 multiples of 2
"""
table = [2*i for i in range(1,11)]
print(table)
"""

# 4.wap to return a list containing 10 multiples of given value(take user input)
"""
n = int(input("Enter an integer: "))
print([n*i for i in range(1, 11)])
"""

# 5.wap to take two lists as input and add that elements and return a single lists
# o/p: l1[1,2,3]; l2[23,44,55] = [12, 14, 16, 18]
"""
l1 = eval(input())
l2 = eval(input())
s = [sum(i) for i in zip(l1,l2)]
print(s)
"""

# 6.wap to create a list containing tuples having two elements that is index and value of list
"""
l=["hey","hello","good","evening","python"]
# normal way
l2 = []
for i in enumerate(l):
    l2.append(i)
print(l2)

# list comp
print([i for i in enumerate(l)])
"""

# 7.wap to check length of strings present in tuple,if length is even append as it is ,else reverse it and append
# """
l=("hey","hello","good","evenings","python")
l2 = []
for i in l:
    if len(i)%2 == 0:
        l2.append(i)
    else:
        l2.append(i[::-1])
print(l2)
print([i if len(i)%2 == 0 else i[::-1] for i in l])
# """