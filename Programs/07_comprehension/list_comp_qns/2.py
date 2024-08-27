# 2.wap to check elements inside the collection are even or odd,if it is even make it square of that numbers,if it is odd make it as cube of that numbers

l=[2,3,5,1,7,2,3]

res = [i**2 if i%2==0 else i**3 for i in l]
print(res)