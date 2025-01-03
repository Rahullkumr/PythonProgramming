import numpy as np

# check version of numpy
print(np.__version__)



# list
l = [1,23,4]



# arrays
one_d = np.array([100])
one_d = np.array([1,2,3])
two_d = np.array([[1,2,3],[7,8,9]])
three_d = np.array([[[3,4,5],[5,6,7], [11,12,13]]])
print(one_d)
print(two_d)
print(three_d)

print(three_d.ndim, ' dimensional')
x = np.arange(1,10,1)
print(x)
print(np.arange(0,20,2))





# range vs arange
'''
1. when we are using range(), we need to typecaste to get proper output.
  no need of typecaste
2. range() can only create only integer value b/w given range.
    arange() will give both int+float
3. range() creates sequence of int numbers b/w the given range
  no sequence is created  
'''

x = np.array([1,2,3,4,5,6,7,8,9,9,11,11,22,33,44])
print(x.shape)  # no of elements present

print(x.reshape(3,5))   # converts 1D to required row-column format i.e (rows, columns)


ls = np.linspace(1,10,4) # jumping 4-1 = 3
print(ls) # [ 1.  4.  7. 10.]

ls = np.linspace(1,10,4, retstep=True) # will also give jumping step
print(ls) # (array([ 1.,  4.,  7., 10.]), 3.0)


list_of_1s = np.ones(5) # array of 5 1s
print(list_of_1s)

o = np.ones((3,4)) # array of 1s in 3rows 4columns format
print(o)
print(o.ndim)
print(o.dtype)
print(type(o))

list_of_1s = np.zeros(5) # 1D array of 5 1s
print(list_of_1s)

o = np.zeros((10,10)) # array of 1s in 10rows 10columns format
print(o)





# diagonal
d = np.identity(5)  # 5rows 5columns
print(d)
print(d.ndim)
print(d.dtype)
print(type(d))