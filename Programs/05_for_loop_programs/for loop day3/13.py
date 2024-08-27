# 13.WAP to print sum of internal and external list

l = [[1,2,3], [4,5,6], [7,8,9]]

# output:
   #internal = 6, 15, 24
   #external --> 45

# solution
'''
internal = []
for i in l:
   internal.append(sum(i))
external = sum(internal)
print(*internal) # * for removing round bracket i.e []
print(external)
'''
# sir's code

res = []
for i in l:
   sum_internal = 0
   for j in i:
      sum_internal += j
   res.append(sum_internal)


print(res);