#  BASIC PROTOCOLS:
        # __getitem__
        # __setitem__
        # __delitem__
        # __contains__
        # __len__



# =========================================

# __getitem__

# class Point:
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
#
#     def __getitem__(self, index):
#         if index == 0:
#             print(self.a)
#         elif index == 1:
#             print(self.b)
#         else:
#             raise IndexError
#
# t = Point(10,20)
# print(t.a)
# print(t.b)
#
# t.__getitem__(0)
# t.__getitem__(1)
# t.__getitem__(99)


# program2
# class Emp:
#     def __init__(self,ename, esal,eid):
#         self.ename = ename
#         self.esal = esal
#         self.eid = eid
#
#     def __getitem__(self, index):
#         if index == 0:
#             print(self.ename)
#         elif index == 1:
#             print(self.esal)
#         elif index == 2:
#             print(self.eid)
#         else:
#             raise IndexError
#
#
# e = Emp('Rahul', 23456, 101)
# print(e.ename)
# print(e.esal)
# print(e.eid)
#
#
# e.__getitem__(0)
# e.__getitem__(1)
# e.__getitem__(2)
# e.__getitem__(2000)

'''__setitem__'''
'''
class Emp:
    def __init__(self,ename, esal, eid):
        self.ename = ename
        self.esal = esal
        self.eid = eid

    def __getitem__(self, index):
        if index == 0:
            return self.ename
        elif index == 1:
            return self.esal
        else:
            return self.eid

    def __setitem__(self, key, value):
        if key == 0:
            self.ename = value
        elif key == 1:
            self.esal = value
        else:
            self.eid = value


e = Emp('Ram', 12345, 'abc121')
print(e.ename)
print(e.esal)
print(e.eid)

e.__setitem__(0,'Rakesh')
e.__setitem__(1,99999)
e.__setitem__(2, 'asd678')

print(e.__getitem__(0))
print(e.__getitem__(1))
print(e.__getitem__(2))
'''

class Temp:
    def __init__(self, *values):
        self.lst = []

        for value in values:
            self.lst.append(value)

    def __len__(self):
        return len(self.lst)

    def __contains__(self, value):
        if value in self.lst:
            return True
        else:
            return False

    def __getitem__(self, index):
        return self.lst[index]

    def __setitem__(self, index, value):
        self.lst[index] = value

    def __delitem__(self, index):
        del self.lst[index]


t = Temp(1,2,3,[55,77],5,6,'hello')

print(t.__len__())
print(t.__contains__('hello'))
print('element at 0 position : ',t.__getitem__(0))
print(t.__setitem__(5,'five'))
print(t.__getitem__(5))

print(t.lst)
print(t.__delitem__(4))
print(t.lst)

























