# Insertion sort

'''
It is a type of sorting algorithm where the current value will get compared to previous value

STEPS:
    s1: consider a list to be sorted
    s2: start iterating from 1 because at 0th pass there will be no value to compare
    s3: check whether i!=0 or not; if true, check whether the current value is < previous value
    s4: if above condition is also true, swap both the values and decrement values of i by 1
    s5: repeat the steps from s3 to s4 for all the passes to get the sorted collection
'''



l = [10, 7, 3, 11, 2]
print('Original: ', l)

for iteration in range(1, len(l)):
    i = iteration
    while i != 0:
        if l[i-1] > l[i]:
            l[i-1], l[i] = l[i], l[i-1]
        i -= 1
print(l)



# task
'''
a = [('akash', 1200), ('vijay', 10000), ('alex', 8000), ('lakshmi', 6000)]
# o/p ==> [('akash', 1200), ('lakshmi', 6000), ('alex', 8000), ('vijay', 10000)]

for iteration in range(1, len(a)):
    i = iteration
    while i != 0:
        if a[i-1][1] > a[i][1]:
            a[i-1], a[i] = a[i], a[i-1]
        i -= 1
print(a)
'''

# Insertion sort me jaise jaise aage badhte jate hn waise waise sorting hoti jati hai
# left side elements are sorted till all gets sorted