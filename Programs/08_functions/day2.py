# def add(parameter bolte hn):
#     pass

# add(argument bolte hn)

# def details(a=0, b=0, c=7):
#     print(a*b*c)
# details()
# details(1)
# details(1,2,3) # 1x2x3

# Variable Scope
# 1. Local Variable (INSIDE A FN ONLY; not inside any if or for or while)
# def a():
#     x = 10
#     print(x)
# a()
# # print(x) error

# 2. Global variable (accessible anywhere)

# x = 100
# def hi():
#     global x
#     x = x+900
#     print(x)

# hi()
# x = x + 400
# print(x)

# 3. Non-local variable
outer = 100
def pythonm():
    # print(outer)
    # print(inner) # UnboundLocalError: cannot access local variable 'inner' where it is not associated with a value
    inner = 111 # ...
    def java():
        nonlocal inner # it must be first stmt
        # print(outer)
        print(inner)
        var = 999
        inner = 'rahul'
        print(inner)
    java()
pythonm()
# print(outer)
# print(inner) # NameError: name 'inner' is not defined.