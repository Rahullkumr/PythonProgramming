import numpy as np

# arithmetic operations in arrays
x = np.array([1,2,3,4])
y = np.array([4,5,6,7])

sum = np.add(x,y)
diff = np.subtract(x,y)
mul = np.multiply(x,y)
div = np.divide(x,y)

print(sum,diff,mul,div)





# statical operations of numpy
y = np.array([11,12,13])
print(np.sum(y))     # sum of all values
print(np.median(y))     # middle value
print(np.std(y))     #  value





# scalar operation
x = np.array([1,2,3,4])
y = np.array([4,5,6,7])
print('arr: ',x)
print('arr: ', y)
x = x+5
y = y+10
print('updated arr: ',x)
print('updated arr: ', y)





# append
a = np.array([11,12,13])
b = np.append(a,99)
print(b)





# insert at particular position
c = np.insert(a,0,555)
print(c)
d = np.insert(a,0, (100,300))
print(d)





# delete 555
a = np.insert(a,0,555)
deleted_arr = np.delete(a,1)
print(deleted_arr)




# random
print('==========')
x = np.random.randint(10)
print(x)
print('=======')
y = np.random.randint(10,size=3)
print(y)
print('==========')
c = np.random.choice([1,2,3,4,5,'regular'])
print(c)





# log values
print('=======')
x = np.array([1,2,3,4,5,9,10])
y = np.log2(x)
print(y)





# lcm
a = 3
b = 12
print('lcm is: ', np.lcm(a,b))
