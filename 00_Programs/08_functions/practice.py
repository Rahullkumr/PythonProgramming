# Function returns in tuple format if we return multiple values

# 1. 
# # op: print only even length words using 08_functions
# x = ['walmart', 'India', 'snap', 'chat', 'fb', 'insta', 'whatsapp', 'group']

# def even_len(x):
#     el = []
#     for i in x:
#         if len(i) % 2 == 0:
#             el.append(i)
#     return el

# print(even_len(x))

# 2.
# Palindrome


# 3
# def add(a,b):
#     print(a+b)

# add(1,2)
# add(1,2,3,4,5,6) # TypeError: add() takes 2 positional arguments but 6 were given

# 4
# def add(*args):
#     print(args)
# add(1,2,3,4,5,6)

# 5.
# def add(x,y):
#     print(x+y)
# add(y=6, x=22)

# 6. kwargs
# def disp(**kwargs):
#     print(kwargs) # 
# disp(a=4,b=6,c=11,d='hello')

def combi(*args, **kwargs):
    print(args, kwargs) # (10, 22, 33) {'a': 4, 'b': 6, 'c': 11, 'd': 'hello'}

combi(10, 22, 33, a=4,b=6,c=11,d='hello')

# 
s={1,2,3,3,6}
print(s)
s.add('new')
print(s)