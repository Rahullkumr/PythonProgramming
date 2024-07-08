import os
# print(os.getcwd())

# os.chdir(r'/workspaces/PythonProgramming/file_handling_kachra') # for github codespace
os.chdir(r'C:\Users\hp\Desktop\PythonProgramming\file_handling_kachra') # for local vscode
# if you need to do CRUD in a particular path then you must goto that path first using os.chdir() i.e use above syntax



# with open('boxoffice.txt', 'w') as file:
    # print(file.read())
    # print(file.readlines())
    # print(file.read(2)) # only two characters
    # print(file.write('day 3 class'))
    # print(file.writelines(['a\n','b\n','c\n']))
    # print(file.write('good day'))
# os.popen('boxoffice.txt')






with open('deleteme.txt', 'r') as file:
    print(file.read())
    print()
    print(file.tell())
    print(f'Cursor is at {file.tell()}th position')  # tells at what index the cursor is present
    print(file.seek(40))
    print(f'Cursor moved {file.seek(40)} positions') # moves the cursor specified no of steps
    print(file.read())








# syntax: ISLICE()

""" 
from itertools import islice
with open('filename', 'mode') as file:
    var_name = islice(iterable, si, ei, sv) # ei = ei-1
"""

# from itertools import islice
# with open('boxoffice.txt', 'r') as file:
#     data = islice(file,0,4,2)
    # print(list(data)) # typecasting is must else will give OBJECT address
    # for i in data: #looping else will give OBJECT address
    #     print(i)







# syntax: DEQUE

"""
from collections import deque
with open('filename', 'mode') as file:
    var_name = deque(iterable, maxlines)
"""

# from collections import deque
# with open('boxoffice.txt', 'r') as file:
#     data = deque(file,2)    # last two lines
#     print(data)