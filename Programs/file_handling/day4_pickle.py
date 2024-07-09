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