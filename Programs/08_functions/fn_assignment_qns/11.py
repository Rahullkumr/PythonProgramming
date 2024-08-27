# 11.wap to check given iterable is a sequence,if it is a sequence reverse it,if not add one extra element to the iterable
def check(x):
    if isinstance(x,(str,list,tuple)): 
        print(x[::-1])
    else:
        # set, dictionary
        if isinstance(x,set):
            x.add(input('Insert new value into the set: '))
            print(x)
        elif isinstance(x,dict):
            k = input('insert key: ')
            v = input('insert value: ')
            x[k] = v
            print(x)
        else:
            print("Enter collection data type")
x = eval(input("Enter any sequence: "))
check(x);