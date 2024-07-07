import os

# print(os.getcwd())
os.chdir(r'C:\Users\hp\Desktop\PythonProgramming\file_handling_kachra') 
# if you need to do CRUD in a particular path then you must goto that path first using os.chdir() i.e use above syntax

# os.mkdir('foldername')
# os.rmdir('foldername')
# print(os.listdir())
# os.rename('folder1', 'renamed_folder') # for both files and folders
# os.popen('deleteme.txt') # only files; error if absent
# os.remove('deleteme.txt') # any kind of file
print(os.path.getsize('pythonbatch.txt')) # both file and folder