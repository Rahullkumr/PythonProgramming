import numpy as np

td = np.array([[1,2,3,3,6,4],[5,6,7,11,2,33]])
print(td)

# slicing
print(td[1][0:6:2])






# iterating an array
'''
Iteration is displaying each element of an array. Here we will see how to iterate 
through Numpy arrays using loops and other method, 
* iterate One-dimensional Numpy array
* iterate two-dimensional Numpy array
* iterate three-dimensional Numpy array
'''

a = np.array([100,200,300,400,500])
for i in a:
    print(i)

a2d= np.array([[1,2,3],[5,6,7]])
for i in a2d:
    # print(i)
    for j in i:
        print(j, end=' ')
    print()

print('::::::::::::::::::::::::::')
a3d = np.array([[[1,2,3], [5,6,7], [4,5,6]]])
print(a3d.ndim)
for i in a3d:
    print(i,end=' ')
    for j in i:
        print(j, end=' ')
        for k in j:
            print(k, end=" ")
        print()
    print()









# joinging/concatenating two arrays using concatenate()
print('============================================')
a1 = np.array([1,2,3,4,5])
a2 = np.array([9,8,7,6,5])
print('before joining')
for i in a1:
    print(i,end=' ')
print()
for j in a2:
    print(j, end=' ')
print()

print('\nafter joining using concatenate()')
x = np.concatenate((a1,a2))
print(x)
print("dimension: ",np.ndim(x))











# joinging/concatenating two arrays using stack()
print('\njoining using stack()')
y = np.stack((a1,a2), axis=1)
print(y)
print("dimension: ",np.ndim(y))









# joinging/concatenating two arrays using vstack()
print('\njoining using vstack()')
y = np.vstack((a1,a2))
print(y)
print("dimension: ",np.ndim(y))









# joinging/concatenating two arrays using hstack()
print('\njoining using hstack()')
y = np.hstack((a1,a2))
print(y)
print("dimension: ",np.ndim(y))










# joinging/concatenating two arrays using dstack()
print('\njoining using dstack()')
y = np.dstack((a1,a2))
print(y)
print("dimension: ",np.ndim(y))











# joinging/concatenating two arrays using column_stack
print('\njoining using column_stack()')
y = np.column_stack((a1,a2))
print(y)
print("dimension: ",np.ndim(y))
print()











# spliting an array (no of elements must be even)
# split vs rsplit
print('\n')
arr = np.array([11,2,3,44,5,77,6,3])
splited_arr = np.split(arr, 2) # splits the array in two parts
print(splited_arr)










# searching a number in the array
san = np.array([11,2,3,44,5,11,11,6,3])
sm = np.where(san == 11)
print(sm)









# intersection
print('\nintersection: finding similar elements')
s1 = np.array([1,2,3,4])
s2 = np.array([12,3,1,7])
print(np.intersect1d(s1,s2))









# dis-similar elements
print('\nsetdiff1d: finding dis-similar elements')
set1 = np.array([1,2,3,4])
set2 = np.array([1,2,3,7])
dis = np.setdiff1d(set2,set1)
print(dis)









# sorting an array
print('\nsorting an array')
ar = np.array([1,2,3,4,4,3,55,22,44,6,77,9])
print(np.sort(ar))

