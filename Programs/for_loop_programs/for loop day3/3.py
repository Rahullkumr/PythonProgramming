# 3.wap if number is even then print its square else print its cube

c=[2,4,5,3,7,9]
l = []
for i in c:
    if i % 2 == 0:
        l.append(i**2)
    else:
        l.append(i**3)

print(l)