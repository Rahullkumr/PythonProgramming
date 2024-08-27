import re 

#1.matches any number between 0-9
"""
a="The cost of the book is Rs.100"
print(re.findall('[0-9]', a))
print(re.findall('[0-9]+', a))

print(re.findall('\d', a))
print(re.findall('\d+', a))
"""



#2.matches only lower case letter and upper case letter
"""
b="hello HOW ARE YOU"
print(re.findall('[a-z]', b))
print(re.findall('[a-z]+', b))

print(re.findall('[A-Z]', b))
print(re.findall('[A-Z]+', b))
"""



#3.write a program to count the number of white space in a given string
"""
c="HELLO world welcome to python Hi how are you. Hi how are you"
print(len(re.findall('\s', c)))
print(len(re.findall(' ', c)))
print(len(re.findall('\W', c)))
"""


#4.sum all the numbers in the below string
"""
word="PYTHON12nREG567exp2"
n = re.findall('[0-9]', word)
n = [int(i) for i in n]
print(sum(n))
"""


#5.matches everything apart from numbers between 0-9
"""
a="The cost of the book is Rs.100"
print(re.findall('\D+', a))
"""


#6.matches everything apart from "a","b","c","d"
"""
b="abcdefghijklmnop"
print(re.findall('[^abcd]',b))    
"""



#7.matches only those characters accepts digit
"""
word="@hello12world34welcome!123"
print(re.findall('\D',word))    # everything apart from digits
"""


#8.extracting file with extension
"""
s="Downloading archive.zip file to download folder python hero.py and afternoon.txt and slicing.jpeg"
print(re.findall('[a-z]+\.[a-z]+',s))
"""



#9.wap to extract only pincode
"""
s="Bangalore pincode is 560001 and area code is BSK234567 and state code is KAR123"
print(re.findall('[0-9]{6}',s))
"""
# /b(boundry) /d(only digits)





# 10.wap to print the AADHAR CARD numbers
"""
s="my aadhar number is 1234-4567-8910"
print(re.findall('[0-9]{4}-[0-9]{4}-[0-9]{4}', s))
"""





# 11.wap to print the pan card number
"""
a="my pan number is ABCDE1234X and other number is PQRST5678W and id is 123abcd45"
print(re.findall(r'[A-Z]{5}[0-9]{4}[A-Z]{1}',a))
"""




# 12.How to fetch the protocols
a="https://www.google.com"
# o/p--->['https', 'www', 'google', 'com'] (i want first output like this )
# o/p--->['https://www.google.com']        (second output)

# """
print(re.findall('[a-z]+',a))
print(re.findall('.+',a))

# """





# 13.creating acronyms of the file format
"""
file_format=["Graphic Interchange Format","Advanced Audio Coding","HyperText Markup Language","Content Management System","Windows Media,Audio","Comma Separated Values"]


# o/p-->GIF,AAC,HTML,CMS,WMA,CSV

for i in file_format:
    match = re.findall('[A-Z]', i)
    # print(match)
    print(''.join(match), end=" ")
"""




# 14.wap to match email ids
"""
emails=["test.user@company.gov","test_user@company.edu","123test-T.user@company.in","testing@company","pspider@company.in"]

for i in emails:
    x=re.findall(r'^[a-zA-z._%+-]+@[a-z]+\.[a-z]+',i)  
    if x:
        print(x)
"""





# 15.matching phone numbers
"""
phonenumbers=["123-345-0987","456-9832-098","800-987-4756","080-1029384727","123-345-12","900-938-0987"]

for i in phonenumbers:
    ph = re.findall('[0-9]{3}-[0-9]{3}-[0-9]{4}', i)
    if ph:
        print(ph)
"""





# 16.replace whitespace with newline characters
"""
s="helloworld welcome to python"
print(re.sub(' ','\n',s))
"""





# 17.replace all digits with **
"""
s="hello 123 mic testing 123 123"
print(re.sub('\d','*',s))
"""