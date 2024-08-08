# """Regular Expression"""

import re
s = 'good day'

# # match
# x = re.match('good', s)
# print(x)
# print(x.start())
# print(x.end())
# print(x.group())

# # fullmatch
# print(re.fullmatch('good day', s))
# print(re.fullmatch('good', s))

# # search
# var = re.search('d', s)
# print(var)

# sub
x = re.sub('o','%',s,3)
print(x)
y = re.subn('o','#',s,4)
print(y)

# # split
# x = re.split('o', s, 1)
# print(x)

# # findall
# s = '123good day888 guys'

# x = re.findall('[0-9]', s)
# print(x)

# x = re.findall('[0-9]+', s)
# print(x)

# # \s \d \D \w(no special char) \W 