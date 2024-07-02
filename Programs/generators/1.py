# 1. wap to generate a+b,a-b,a*b,a/b by taking a and b from user

def operation(a,b):
    yield a+b
    yield a-b
    yield a*b
    yield a/b 


a = int(input("Enter first no: "))
b = int(input("Enter second no: "))
out = operation(a,b)
print(next(out))
print(next(out))
print(next(out))
print(next(out))
