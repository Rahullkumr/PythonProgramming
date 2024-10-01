# arithmetical operation using magic methods (NUMBER PROTOCOL)

# __add__
# __sub__
# __mul__
# __div__
# __floordiv__
# __divmod__
# __mod__
# __gt__
# __lt__
# __eq__
# __add__

class Sample:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return self.a+other.a, self.b+other.b

    def __sub__(self, other):
        return self.a-other.a, self.b-other.b

    def __mul__(self, other):
        return self.a*other.a, self.b*other.b

    def __div__(self, other):
        return self.a/other.a

    def __floordiv__(self, other):
        return self.a//other.a, self.b//other.b

    def __divmod__(self, other):
        return self.a%other.a, self.b%other.b

s = Sample(10,20)
s1 =Sample(100,200)

# addition
print(s.__add__(s1))
x = s+s1
print(x)

# subtraction
print(s.__sub__(s1))
subtr = s-s1
print(subtr)

# multiplication
print(s.__mul__(s1))
multi = s*s1
print(multi)

# Division
print(s.__div__(s1))
# divi = s/s1a
# print(divi)

# floordivision (working)
print(s.__floordiv__(s1))

# divmod(# quotient + remainder)
print(s.__divmod__(s1))

# ==============================
print('========__MOD__===============')

class Point:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __mod__(self, other):
        self.a,other.b

p = Point(20,5)
print(p.a % p.b)

print('========__GT__===============')

class Point1:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __gt__(self, other):
        if self.a>other.b:
            return True
        else:
            return False


p = Point1(20,50)
print(p.a > p.b)


print('========__LT__===============')

class Point1:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __lt__(self, other):
        if self.a < other.b:
            return True
        else:
            return False


p = Point1(20,50)
print(p.a < p.b)

print('========__EQ__===============')

class Point1:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __eq__(self, other):
        if self.a == other.b:
            return True
        else:
            return False


p = Point1(20,20)
print(p.a == p.b)






# reminder
# quotient + remainder
# divmod(a,b)


# types of errors (DXC company)
# ========================================
print('========================================')

class All:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def __add__(self, other):
        self.a+other.b

    def __sub__(self, other):
        self.a-other.b

    def __mul__(self, other):
        self.a*other.b

    def __div__(self, other):
        self.a/other.b

    def __floordiv__(self, other):
        self.a//other.b

    def __divmod__(self, other):
        self.a%other.b

    def __mod__(self, other):
        self.a%other.b

    def __gt__(self, other):
        if self.a > other.b:
            return True
        else:
            return False

    def __lt__(self, other):
        if self.a < other.b:
            return True
        else:
            return False

    def __eq__(self, other):
        if self.a == other.b:
            return True
        else:
            return False

obj = All(50,3)
print(obj.a+obj.b)
print(obj.a-obj.b)
print(obj.a*obj.b)
print(obj.a/obj.b)
print(obj.a//obj.b)
print(divmod(obj.a,obj.b))
print(obj.a%obj.b)
print(obj.a > obj.b)
print(obj.a < obj.b)
print(obj.a == obj.b)































