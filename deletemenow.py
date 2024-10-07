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
x = np.array([1,2,3,4,5])
print(x.reshape(1,2))

# array vs series
