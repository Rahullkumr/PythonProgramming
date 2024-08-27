# 1.WAP to replace one string with another string
# s = 'hello world'
# #exp o/p : 'hello Universe
"""
s = 'hello world'
print(f'Original string: {s}')
s = s.replace('hello world', 'hello Universe')
print(f'After replace: {s}')
"""





# 2.WAP to reverse each element in a list,then reverse entire list
# names = ['apple', 'google', 'yahoo', 'walmart']
"""
names = ['apple', 'google', 'yahoo', 'walmart']
names = [i[::-1] for i in names]
print(list(reversed(names)))    # ['tramlaw', 'oohay', 'elgoog', 'elppa']
"""





# 3.WAP to sort the list which is mix of both even & odd,
# the sorted list should have odd numbers first & then even numbers in sorted order
# l = [3, 4, 1, 7, 2, 12, 8, 9, 11, 16, 13]
# o/p
# #odd ->[1,3,7,9,11,13] even-> [2,4,8,12,16]
"""
l = [3, 4, 1, 7, 2, 12, 8, 9, 11, 16, 13]
odd,even = [],[]
for i in l:
    if i%2 != 0:
        odd.append(i)
    else:
        even.append(i)
print(sorted(odd) + sorted(even))   # [1, 3, 7, 9, 11, 13, 2, 4, 8, 12, 16]
"""





# 4. WAP to print maximum sum of 3 numbers & minimum sum of 3 numbers
# numbers = [18,15,20,25, 30,35, 40, 5,10,15]
"""
numbers = [18,15,20,25, 30,35, 40, 5,10,15]
numbers = sorted(numbers)
print(f'sorted nos: {numbers}')
print(f'sum of first 3 minimum numbers: {sum(numbers[:3])}')
print(f'sum of first 3 maximum numbers: {sum(numbers[-3:])}')

# o/p

# sorted nos: [5, 10, 15, 15, 18, 20, 25, 30, 35, 40]
# sum of 3 minimum numbers: 30
# sum of 3 maximum numbers: 105
"""





# 5.WAP to remove duplicates from the list without using empty list or set
# l = [1, 2, 3, 4, 1, 2, 3, 4, 4, 5]
#o/p :[1,2,3,4,5]
"""
def remove_duplicate(l):
    i = 0
    while i < len(l):
        current_no = l[i]
        while l.count(current_no) > 1:
            l.remove(current_no)
        i += 1

l = [1, 2, 3, 4, 1, 2, 3, 4, 4, 5]
remove_duplicate(l)
print(l)        # [1, 2, 3, 4, 5]
"""





# 6.Real time scenario based 13_OOPs
# Requirements:
# ============

# Login into Qspiders class

# username : It should be mail address or phone number
# mail id : It should have 1 @ max of 2 '.' and should ends with .com
# phone number : the length should be 13 including '+'
# pwd: The length should be 8 characters (atleast 1uc, 1lc, 1spl, 1digit)
# """


from abc import ABC, abstractmethod
import re

class User(ABC):
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @abstractmethod
    def is_valid(self):
        pass

class EmailUser(User):
    def is_valid(self):
        email_regex = r'^[\w.-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,4}$'
        return re.match(email_regex, self.username) is not None

class PhoneUser(User):
    def is_valid(self):
        phone_regex = r'^\+\d{12}$'
        return re.match(phone_regex, self.username) is not None

class PasswordValidator:
    def __init__(self, password):
        self.password = password

    def is_valid(self):
        password = self.password

        if len(password) < 8:
            return False

        if not re.findall(r"[a-z]", password):
            return False

        if not re.findall(r"[A-Z]", password):
            return False

        if not re.findall(r"\d", password):
            return False

        if not re.findall(r"[@$!%*#?&]", password):
            return False

        return True

class Login:
    def __init__(self, username, password):
        if '@' in username:
            self.user = EmailUser(username, password)
        else:
            self.user = PhoneUser(username, password)
        self.password_validator = PasswordValidator(password)

    def login(self):
        if self.user.is_valid() and self.password_validator.is_valid():
            print("Login successful")
        else:
            print("Invalid credentials")

username = "abc@example.com"
password = "Password123!"
login = Login(username, password)
login.login()       # Login successful
# """





# 7..WAP to get given o/p:
# l = ['sun flower', 'lilly flower', 'Marigold flower', 'lion animal',
#      'tiger animal', 'eagle bird', 'snake animal', 'lotus flower', 'pigeon bird']
# #exp o/p : {'flower': [sun, lilly, marigold, lotus],
# # 'animal': [lion, tiger, snake], 'bird': [eagle, pigeon]}
"""
l = ['sun flower', 'lilly flower', 'Marigold flower', 'lion animal', 'tiger animal', 'eagle bird', 'snake animal', 'lotus flower', 'pigeon bird']

d = {}
f,a,b = [],[],[]

for i in l:
    category = i.split()[1]
    if category == 'flower':
        f.append(i.split()[0])
    elif category == 'animal':
        a.append(i.split()[0])
    else:
        b.append(i.split()[0])

d['flower'], d['animal'],d['bird'] = f,a,b
print(d)
"""





# 8.WAP to take 2 list remove repeated elements in both & return a list of unique elements without typecasting to set

# l1 = [2, 3, 5, 7, 5, 2]
# l2 = [5, 4, 2, 7, 8, 4, 5]
"""
def remove_duplicate(l):
    without_duplicates = []
    for i in l:
        if i not in without_duplicates:
            without_duplicates.append(i)
    return without_duplicates

l1 = [2, 3, 5, 7, 5, 2]
l2 = [5, 4, 2, 7, 8, 4, 5]
print(remove_duplicate(l1+l2))      # [2, 3, 5, 7, 4, 8]
"""





# 9.WAP to separate vowels & consonants from a string.
# s = 'hello guys good morning welcome to programming class'
# #exp o/p :{'vowels': [e,o,u,o,o..], 'conso':[h,l,l]}
"""
s = 'hello guys good morning welcome to programming class'
vowel_consonant = {}
v,c = [],[]
for i in s:
    if i in ('a','e','i','o','u','A','E','I','O','U'):
        v += i    
    else:
        c += i
vowel_consonant['vowel'] = v 
vowel_consonant['conso'] = c
print(vowel_consonant)
"""





# 10.WAP to suggest a Student to take which course in QSP/JSP/PYSP
# lst = ['QSP', 'JSP', 'PYSP']
# names = ['Testing', 'Development']
"""
lst = ['QSP', 'JSP', 'PYSP']
names = ['Testing', 'Development']

choice = input("choose between 'QSP', 'JSP' and 'PYSP' : ")

if choice in lst:
    print(f'You can take subjects like: {names}')
else:
    print('Enter valid name')
"""