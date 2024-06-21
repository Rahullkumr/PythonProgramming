# 3.WAP to remove duplicates from the list without using inbuilt function

d = [1,2,3,4,5,6,7,1,2,3,4]

# print(set(d))

dup = []
non_dup = []

for i in d:
    if i not in non_dup:
        non_dup.append(i)
    else:
        dup.append(i)

print(dup) # [1, 2, 3, 4]
print(non_dup) # [1, 2, 3, 4, 5, 6, 7]