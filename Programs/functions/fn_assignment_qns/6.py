# 6.wap to squaring of the element in the given list

def square_elements(l):
    l2 = []
    for i in l:
        l2.append(i**2)
    return l2
l=[1,2,3,4,5]
print(square_elements(l))