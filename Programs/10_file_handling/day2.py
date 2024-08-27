import os
# print(os.getcwd())

# os.chdir(r'/workspaces/PythonProgramming/file_handling_kachra') # for github codespace
os.chdir(r'C:\Users\hp\Desktop\PythonProgramming\file_handling_kachra')
# if you need to do CRUD in a particular path then you must goto that path first using os.chdir() i.e use above syntax

# file = open('boxoffice.txt', 'x') # if not present, creates

# FILE ATTRIBUTES

# file1 = open('boxoffice.txt')
# print(file1.name)
# print(file1.mode)
# print(file1.readable())
# print(file1.writable())
# print(file1.close())

# WRITING INTO THE FILE

# x= open('boxoffice.txt', 'a')
# l = ['sunny\n', 'bunny\n', 'sunil\n']
# print(x.writelines(l))

# x= open('boxoffice.txt', 'a')
# print(x.writelines(['good morning\n', 'good afternoon\n']))
# print(x.write('morning python class'))
# os.popen('boxoffice.txt') # opens the file in text editor

# x = open('boxoffice5.txt', 'w')
# print(x.write('hello guys'))
# os.popen('boxoffice5.txt')

file = open('pythonbatch.txt', 'r')
# print(file.read()) # reads entire content 
# print(file.readline()) # reads one line only; whenever it gets \n it stops
print(file.readlines()) # reads entire content and returns inside a list; adds \n wherever there is newline
