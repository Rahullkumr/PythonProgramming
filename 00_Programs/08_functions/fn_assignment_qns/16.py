# 16.waf to return a dictionary with characters and ascii value pair

def func(s):
    d = dict()
    for i in s:
        d[i] = ord(i)

    return d

s = input("Enter a string: ")
print(func(s))