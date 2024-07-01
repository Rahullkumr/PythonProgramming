# 17. waf to reverse an iterable if you are passing string or list or tuple else print type of the data

def check(it):
    if isinstance(it,(str,list,tuple)):
        print(it[::-1])
    else:
        print(type(it))
it = eval(input("Enter string or list or tuple: "))

check(it)