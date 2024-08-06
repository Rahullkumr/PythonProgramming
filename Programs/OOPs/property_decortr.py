"""Best example of encapsulation"""
# class Test:
#     def __init__(self, pdt):
#         self.__pdt = pdt

#     def getter(self):
#         print("Accessing private data using getter method")
#         return self.__pdt

#     def setter(self,pdt):
#         self.__pdt = pdt
#         print('private data set successfully using setter method')


#     def deleter(self):
#         del self.__pdt
#         print('private data deleted using deleter method')

# t = Test('watch')
# print(t.getter())
# t.setter('laptop')
# print(t.getter())
# t.deleter()
# print(t.getter())   # AttributeError: 'Test' object has no attribute 'pdt'

""" =================================================================="""

# property decorator example with single parameter

# class Test:
#     def __init__(self, pdt):
#         self.pdt = pdt

#     @property
#     def getter_(self):
#         return self.pdt
    
#     @getter_.setter
#     def getter_(self,pdt):
#         self.pdt = pdt

#     @getter_.deleter
#     def getter_(self):
#         del self.pdt 

# t = Test('watch')
# print(t.getter_)
# t.getter_ = ('phone')
# print(t.getter_)

# del t.getter_
# print(t.getter_)        # AttributeError: 'Test' object has no attribute 'pdt'

""" =================================================================="""

# property decorator example with multiple parameters

class Test:
    def __init__(self, pdt, price):
        self._pdt = pdt
        self._price = price

    @property               # getter
    def getter_(self):
        return self._pdt, self._price
    
    @getter_.setter
    def getter_(self,details):
        self._pdt, self._price = details

    @getter_.deleter
    def getter_(self):
        del self.pdt 

t = Test('watch', 'laptop')
print(t.getter_)
t.getter_ = ('abc',2000)
print(t.getter_)