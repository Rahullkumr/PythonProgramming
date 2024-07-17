l = [1, 0, 1, 0, 1, 0]

# first approach
l1,l2 = [],[]
for i in l:
  if i == 0:
    l1.append(i)
  else:
    l2.append(i)
print(l1+l2)

# ===========================================

# second approach
# print([0] * l.count(0) + [1] * l.count(1))

# ===========================================

# third approach
# i = 0
# for j in range(len(l)):
#     if l[j] == 0:
#         l[i], l[j] = l[j], l[i]
#         i = i + 1

# print(l)