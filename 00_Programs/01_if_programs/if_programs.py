''' IF CONDITION RELATED PROGRAMS'''


# 1.wap to check the number is odd (take user input)
"""
if int(input("Enter a number: ")) % 2 != 0:
    print('Odd number')
"""

# 2.wap to check the number is even (take user input)
"""
if int(input("Enter a number: ")) % 2 == 0:
    print('Even number')
"""

# 3.wap to check if the student has scored 70%, print "good luck "(take user input)
"""
if int(input("Enter your percentage: ")) == 70:
    print('good luck')
"""

# 4.wap to check which number is greater using if condition
# a=98
# b=67
"""
a=98
b=67
if a>b: print(f'a i.e {a} is greater')
if a<b: print(f'b i.e {b} is greater')
"""

# 5.wap to check if the given string has even length of character
# s="hey guys you all are Osam"
"""
s = "hey guys you all are Osam"         # 25 characters 
if len(s)%2==0: print("Yes it contains even length of characters")
"""

# 6.wap to check if the given number is divisible by 5 (take user input)
"""
if int(input('Enter a number: '))%5 == 0: print('Divisible by 5')
"""

# 7.wap to check if the given programming language is present in the list
# p=["java","python","c","c++","RUBy","golang"]
"""
p=["java","python","c","c++","RUBy","golang"]
if input('Enter programming language to check: ') in p: print('PRESENT')
"""

# 8.wap to check eligible to vote take user input as a age
"""
if int(input('Enter age to check voter eligibility: ')) >= 0: print('ELIGIBLE')
"""

# 9.wap to check if the given number is positive take user input
"""
if int(input('Enter any number to check positivity: ')) >= 0: print('POSITIVE')
"""

# 10.wap to check if the given string is palindrome (take user input)
"""
word = input('Enter a word: ')
if word == word[::-1]: print('PALINDROME')
"""

# 11.wap to check if the first letter in the given string is consonant
# s="Lahari is a good student"
"""
s = "Lahari is a good student"
if s[0] not in ('aeiouAEIOU'): print(f'{s[0]} is CONSTANT')
"""

# 12.wap to check the given string is uppercase or not (take user input)
"""
if input('Enter a string: ').isupper(): print('upper case')
"""

# 13.wap to check the given value is string (take user input)
"""
if isinstance(eval(input('Enter a string: ')),str): print('Yes, it is string')
"""

# 14.wap to display "Python Coding" if the number is greater than 1 and less than 5 (take user input)
"""
if 1 < int(input('Enter a number: ')) < 5: print('Python Coding')
"""

# 15.wap to check whether given number is negative and print "its negative guys"
"""
if int(input('Enter a number: ')) < 0: print('its negative guys')
"""

# 16.wap to check whether given input is divisible by 2 and 6.
# If condition is True, convert the given number to complex number.(take user input)
"""
n = int(input('Enter a number: '))
if n%2==0 and n%6==0: print(complex(n))
"""

# 17.wap to check whether the given number is even or not.
# If even store the value inside the list (take user input)
"""
l, n = [], int(input('Enter a number: '))
if n % 2 == 0: l.append(n)
print(l)
"""

# 19.wap to check whether a given value is divisible by 5 and 7.
# If the value is divisible then display the square of the values (take user input)
"""
n = int(input('Enter a number: '))
if n%5==0 and n%7==0: print(n*n)
"""

# 20. wap to check whether a given value is present in between 45 and 200 and the number should be divisible by 4 and 5.
# If satisfied,display the ascii characters (take user input)
"""
n = int(input('Enter a number: '))
if 45 < n < 200 and n%4==0 and n%5==0: print(chr(n))
"""

# 21.wap to check if given string contains a substring
# string="hello world"
# sub_string="world"
"""
string="hello world"
sub_string="world"
if sub_string in string.split(): print('PRESENT')
"""

# 22.wap to check whether a character is in the alphabet or not.
# If it is alphabet,store the value inside a dict(key as a character and value as an ascii value)
"""
d = {}
chr = input('Enter a character: ')
if (65 <= ord(chr) <= 90) or (97 <= ord(chr) <= 122): d[chr] = ord(chr)
print(d)
"""

# 23.wap to check whether a character is in uppercase or not.
# If uppercase,convert to lowercase and store the value inside the dictionary (character as key and ascii as value)
# take user input
# """
d,str = {}, input('Enter a string: ')
if str.isupper(): d[str] = str.lower()
print(d)
# """
