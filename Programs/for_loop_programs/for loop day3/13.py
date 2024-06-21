# 13.WAP to print sum of internal and external list

l = [[1,2,3], [4,5,6], [7,8,9]]

# output:
   #internal = 6, 15, 24
   #external --> 45
internal = []

for i in l:
   internal.append(sum(i))

external = sum(internal)
print(*internal) # * for removing round bracket symbol i.e []
print(external)