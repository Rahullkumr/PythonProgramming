# 2.Print all the missing numbers from 1-10 in the below list

l = [1, 2, 3, 4, 6, 7, 10]

for i in range(1, 11):
    if i not in l:
        print(i)