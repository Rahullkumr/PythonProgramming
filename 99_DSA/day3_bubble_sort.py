# Sorting algorithms:

'''
1. Bubble sort:
    It is a type of sorting algorithm, where each and every value will be swapped based on condition to arrange/present it in sorted manner
    In this case we can perform, n-1 passes where n = length of input collection
    In each and every pass, one value will get sorted into respective sorted position
'''

x = [23, 6, 9, 3, 10, 11]
print('original: ', x)

for i in range(0, len(x)-1):
    if x[i] > x[i+1]:
        x[i], x[i+1] = x[i+1], x[i]
print(x)

for i in range(0, len(x)-2):
    if x[i] > x[i+1]:
        x[i], x[i+1] = x[i+1], x[i]
print(x)

# ==============================================

x = 'apple java sql cpp'
print(x)
x_arr = x.split()

for k in range(1, 3):
    for i in range(0, len(x_arr)-k):
        if x_arr[i] > x_arr[i+1]:
            x_arr[i], x_arr[i+1] = x_arr[i+1], x_arr[i]
print(' '.join(x_arr))

# ==================================================
# s = 'apple atom bat cat elephant vijay'
# s_splitted = s.split(' ')
# for no in range(1, len(s_splitted)):
#     for i in range(0, len(s_splitted)-no):
#         if s_splitted[i] > s_splitted[i+1]:
#             s_splitted[i], s_splitted[i + 1] = s_splitted[i+1], s_splitted[i]
#
# print(' '.join(s_splitted))

#
s = 'python hello programming hai smille'
s_splitted = s.split(' ')
for no in range(1, len(s_splitted)):
    for i in range(0, len(s_splitted)-no):
        if s_splitted[i] > s_splitted[i+1]:
            s_splitted[i], s_splitted[i + 1] = s_splitted[i+1], s_splitted[i]
print(' '.join(s_splitted))
