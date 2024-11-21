# class  Test:
#   '''doc string is written here'''
#   a = 3
#   b = 5
  

# print(Test.__doc__)     # docstring of the class is printed



# obj = Test()
# print(obj)  # obj address

# class_alias = Test
# print(class_alias) # refers to class; like alias name to class

# print('id of obj = ', id(obj))
# print('id of class_alias variable = ', id(class_alias))
  




# print(Test.__dict__)    # gives internal storage of class elements
"""
{'__module__': '__main__', '__doc__': 'doc string is written here', 'a': 3, 'b': 5, '__dict__': <attribute '__dict__' of 'Test' objects>, '__weakref__': <attribute '__weakref__' of 'Test' objects>}
"""




# help(Test)  # gives details of the class




# Accessing class attributes:
  # - by using ClassName
  # - by using object 

# print(Test.a)
# print(obj.b)

# ==========================================================
# ==========================================================






class Demo:
    a = 10
    b = 20

o1 = Demo()
o2 = Demo()

print("\033[31m", "before modification\n=========", "\033[0m")

print("Demo.a= ",Demo.a)
print("o1.a= ",o1.a)
print("o2.a= ",o2.a)


print()
print("\033[31m", "after modification in class variable\n=========", "\033[0m")
Demo.a = '111'

print("Demo.a= ",Demo.a)
print("o1.a= ",o1.a)
print("o2.a= ",o2.a)


print()
print("\033[31m", "after modification in o1's variable\n=========", "\033[0m")
o1.a = "999"

print("Demo.a= ",Demo.a)
print("o1.a= ",o1.a)
print("o2.a= ",o2.a)


print()
print("\033[31m", "again modification in class variable\n=========", "\033[0m")
Demo.a = 'class var edited 2nd time'

print("Demo.a= ",Demo.a)
print("o1.a= ",o1.a, " DEKH RHE HO CONNECTION LOSS")
print("o2.a= ",o2.a)
print()