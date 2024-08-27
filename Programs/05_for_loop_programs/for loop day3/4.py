# 4.wap to create a list with square and cube of each numbers

d=[2,4,5,1,8,9,10]

# o/p-->[(4, 8), (16, 64), (25, 125), (1, 1), (64, 512), (81, 729), (100, 1000)]
l = []

for i in d:
    l.append((i**2, i**3))

print(l)