'''
WAP to print character and index pair without using inbuilt function
output:
0 p
1 y
2 t
3 h
4 o
5 n
'''
s = "python"
for i in range(0, len(s)):
    print(i, s[i])

# using inbuilt function
    
print(list(enumerate(s)))

# [(0, 'p'), (1, 'y'), (2, 't'), (3, 'h'), (4, 'o'), (5, 'n')]

