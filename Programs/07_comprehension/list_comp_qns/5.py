# 5.wap to take two lists as input and add that elements and return a single lists
# o/p: l1[1,2,3]; l2[23,44,55] = [12, 14, 16, 18]

l1 = eval(input())
l2 = eval(input())
s = [sum(i) for i in zip(l1,l2)]
print(s)