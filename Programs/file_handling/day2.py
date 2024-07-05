import os
# print(os.getcwd())

#os.chdir(r'C:\Users\hp\Desktop\PythonProgramming\Programs\file_handling')
# print(os.getcwd())

#file = open('boxoffice.txt', 'x') # if not create

# file1 = open('boxoffice.txt')

# file attributes
#print(file1.name)
#print(file1.mode)
#print(file1.readable())
#print(file1.writable())
#print(file1.close())

# writing into the file
'''
x= open('boxoffice.txt', 'a')
l = ['sunny\n', 'bunny\n', 'sunil\n']
print(x.writelines(l))
'''

x= open('boxoffice.txt', 'a')
print(x.writelines(['good morning\n', 'good afternoon\n']))
print(x.write('morning python class'))

os.popen('boxoffice.txt')

x1 = open('boxoffices.txt', 'w')
print(x1.write('hello guys'))

os.popen('boxoffice5.txt')

x2 = open('boxoffice15.txt', 'a')
print(x2.write('boxoffice days'))

os.popen('boxoffice15.txt')

file = open('pythonbatch.txt', 'r')

print(file.read())
print(file.readline())
print(file.readline())
print(file.readlines())