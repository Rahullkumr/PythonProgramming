# 7.wap to check length of strings present in tuple,if length is even append as it is ,else reverse it and append


l=("hey","hello","good","evenings","python")
l2 = []
for i in l:
    if len(i)%2 == 0:
        l2.append(i)
    else:
        l2.append(i[::-1])

print(l2)

print([i if len(i)%2 == 0 else i[::-1] for i in l])