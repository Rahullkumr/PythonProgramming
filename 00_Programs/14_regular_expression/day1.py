# """Regular Expression"""

import re
s = 'good day'

# match
"""
x = re.match('good', s)
print(x)
print(x.start())
print(x.end())
print(x.group())
"""




# fullmatch
"""
print(re.fullmatch('good day', s))
print(re.fullmatch('good', s))
"""




# search
"""
var = re.search('d', s)
print(var)
"""




# sub
"""
x = re.sub('o','%',s,3)
print(x)
y = re.subn('o','#',s,4)
print(y)
"""






# split
"""
x = re.split('o', s, 1)
print(x)
"""




# findall
"""
s = '123good day888 guys'

x = re.findall('[0-9]', s)
print(x)

x = re.findall('[0-9]+', s)
print(x)
# """ 





# wap to match a user input mobile number with the following condition using regular expression
# it must be 10 digit, it must start with 7 or 8 or 9

import re

def validate_mobile_number(mobile_number):
    pattern = r'^[789]\d{9}$'
    return True if re.match(pattern, str(mobile_number)) else False 

# Taking user input
mobile_number = 9711115265
# mobile_number = 9711165
# mobile_number = 1711115265

# Validating the mobile number
if validate_mobile_number(mobile_number):
    print("Valid mobile number.")
else:
    print("Invalid mobile number. It must be a 10-digit number starting with 7, 8, or 9.")
