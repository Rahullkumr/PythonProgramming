import os
# print(os.getcwd())

os.chdir(r'/workspaces/PythonProgramming/file_handling_kachra') #to be used in codespace only
# if you need to do CRUD in a particular path then you must goto that path first using os.chdir() i.e use above syntax

# with open('boxoffice.txt', 'w') as file:
    # print(file.read())
    # print(file.readlines())
    # print(file.read(2)) # only two characters
    # print(file.write('day 3 class'))
    # print(file.writelines(['a\n','b\n','c\n']))
    # print(file.write('good day'))

# os.popen('boxoffice.txt')

# islice

# from itertools import islice
"""
syntax: with open('filename', 'mode') as file:
            var_name = islice(iterable, si, ei, sv)
"""

# with open('boxoffice.txt', 'r') as file:
#     data = islice(file,0,4,2)
#     # print(list(data)) # typecasting is must else will give OBJECT address

#     for i in data: #looping else will give OBJECT address
#         print(i)

# deque
from collections import deque
"""
syntax: with open('filename', 'mode') as file:
            var_name = deque(iterable, line)
"""
with open('boxoffice.txt', 'r') as file:
    data = deque(file,2)
    print(data)