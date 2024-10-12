import numpy as np

# copy() vs view()
# x = np.array([1,2,3,4])
# y = x.copy()
# x[0] = 99
# print(id(x))
# print(id(y))


#
# z = x.view()
# q = z
# print("\n",id(z))
# print(id(q))

# convert 1D array to nD Array
# x = np.array([1,2,3,4,5])
# print(x.reshape(1,2))

# array vs series
# =============


# arr = [3456,678,345]

# arr.ndim
# arr.shape
# arr.size
# arr.dtype

# a = np.array([1,2,"hello", True]) # works for all collection data types
# print(a)
#
#
# for i in range(1.3, 5.5, 1):
#     print(i)        # TypeError: 'float' object cannot be interpreted as an integer

"""
x = np.arange(1,17)
print(x)

y = x.reshape(2,2,4)  # 2(matrices) 2(row) 4(column)
print(y)

# o/p (2D)
'''
[[[ 1  2  3  4]
  [ 5  6  7  8]]

 [[ 9 10 11 12]
  [13 14 15 16]]]
'''


z = x.reshape(2, 2, 2, 2)  # 2(cluster) 2(matrices) 2(row) 2(column)
print(z)

'''
[[[[ 1  2]
   [ 3  4]]

  [[ 5  6]
   [ 7  8]]]


 [[[ 9 10]
   [11 12]]

  [[13 14]
   [15 16]]]]
'''


uda = np.full((2,3,3),'python')
print(uda)
'''
[[['python' 'python' 'python']
  ['python' 'python' 'python']
  ['python' 'python' 'python']]

 [['python' 'python' 'python']
  ['python' 'python' 'python']
  ['python' 'python' 'python']]]
'''

a = np.array([1, 2, 3])
print(id(a))

c = a.copy()
v = a.view()
print(c)
print(v, '\n')

c[0] = 99
print(a)
print(id(c))

v[0] = 11
print(a, '\n')
print(id(v))

print(c)
print(v)

# numerical opoerations

a1 = np.array([1, 2, 3, 4, 5])
a2 = np.array([9, 8, 7, 6, 5])


print('\njoining using stack()')
y = np.stack((a1,a2), axis=1)
print(y)
print("dimension: ",np.ndim(y))



print('\njoining using vstack()')
y = np.vstack((a1, a2))
print(y)
print("dimension: ", np.ndim(y))


print('\njoining using dstack()')
y = np.dstack((a1,a2))
print(y)
print("dimension: ",np.ndim(y))



print('\njoining using cstack()')
y = np.column_stack((a1,a2))
print(y)
print("dimension: ",np.ndim(y))
"""

# 4D to 1D array using flatten

# ===============================

x = np.array([
    [1,2,3],
    [18, 4, 6]
])

print(x.min(axis=0))        # [1 2 3]
print(x.min(axis=1))        # [1 4]
print(x.max(axis=0))        # [18  4  6]
print(x.max(axis=1))        # [ 3 18]


#
x = np.array([1,2,3])
a = np.append(x, [78, 100, 200])
print(a)


i = np.insert(x, 0, [99,88])
print(i)

d = np.delete(i, [1, 2])
print(d)

# linspace

l = np.linspace(1,10,3,retstep=True)
print(l)

# defdiff1d
x = np.array([1, 2, 3, 4])
y = np.array([11, 2, 3, 14])

s = np.subtract(x,y)
print(s)

#
# std = np.std(x, y)
# print(std)

print('-------------------------------------')

r = np.random.rand()
print(r)

r = np.random.rand(5)
print(r)


r = np.random.randint(2)
print(r)


r = np.random.uniform(2)
print(r)








