'''
Data: is a raw fact whereas information is a processed data.


Data Structure:
    It is a phenomenon of giving the str to the data (storing the data in an organised format)

why do we use DS:
    using DS, it is easy to get the value back.

Complexity measure:
    It is a phenomenon of measuring the total space consumed or the total time taken by the program for its execution
    1. space complexity
    2. time complexity

1. Space complexity:
    It is a phenomenon of measuring the total space consumed by the program for its execution
    eg1:
        a = 10
        b = 20
        sum = a + b
        print(sum)
    eg2:
        a = 10
        b = 20
        print(a+b)


2. Time complexity
    It is a phenomenon of measuring the total time taken by the program for its execution
    eg:
        import time
        start = time.time()
        s = eval(input('Enter the data'))
        out = s[::-1]
        print(out)
        end = time.time()
        print(end-start)

Time complexity measure, we have 3 types:
    1. worst time complexity
    2. Average time complexity
    3. Best time complexity

1. worst case time complexity
    It is a maximum time taken to execute the program where result can be either positive or negative
    eg:
        a = [1,3,5,2,7,8]
        key = 8     ===> +ve o/p
        key = 123   ===> -ve o/p

2. Average time complexity
    It is the average time taken to get the +ve response
    It will always lie between Best time complexity and Worst time complexity
    eg:
        a = [1,3,5,2,7,8]
        key = 3
        key = 2

3. Best time complexity
    It is the minimum time taken to get the +ve response
    eg:
        a = [1,3,5,2,7,8]
        key = 1


'''

# import time
#
# start = time.time()
# s = eval(input('Enter the data: '))
# out = s[::-1]
# print(out)
# end = time.time()
# print(end - start)

# homework
# worst time and best time (search for smallest no)
a = 100
b = 33
c = 20

if a<b and a<c:
    print(f'{a} is the smallest')
elif b<c:
    print(f'{b} is the smallest')
else:
    print(f'{c} is the smallest')

'''
worst case time complexity => a,b,c = 100, 35, 20
best case time complexity  => a,b,c = 20, 35, 100
'''
# syllabus:
    # searching
    # sorting
    # ll
    # stack
    # queue
    # tree



