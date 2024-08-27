import os
# print(os.getcwd())

# os.chdir(r'/workspaces/PythonProgramming/file_handling_kachra') # for github codespace
os.chdir(r'C:\Users\hp\Desktop\PythonProgramming\file_handling_kachra') # for local vscode
# if you need to do CRUD in a particular path then you must goto that path first using os.chdir() i.e use above syntax

# pickle

import pickle
with open('lastday.pkl','wb') as file:
    data = pickle.dump('helloworld', file)
os.popen('lastday.pkl')

# with open('lastday.pkl', 'rb') as file:
#     data = pickle.load(file)
#     print(data)

# os.popen('lastday.pkl')

"""
- Pickling is serialization; unpickling is deserialization.

Pickling:

It is the process of converting a Python object into a byte stream (a sequence of bytes) 
to store it in a file or send it over a network.
The 'pickle' module is used for this purpose.
eg
import pickle

data = {'name': 'Alice', 'age': 25}
with open('data.pkl', 'wb') as file:
    pickle.dump(data, file)


Unpickling:

It is the reverse process, converting a byte stream back into a Python object.
eg
import pickle

with open('data.pkl', 'rb') as file:
    data = pickle.load(file)
print(data)  # Output: {'name': 'Alice', 'age': 25}
"""