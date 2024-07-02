# wap to generate only values which are divisible by 5
l = [34,55,60,56,78,90,25,40]

def multiply():
    l2 = []
    for i in l:
        if i % 5 == 0:
            l2.append(i)
    yield l2

output = multiply()
print(next(output))