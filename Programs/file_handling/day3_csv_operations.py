import os
print(os.getcwd())

# os.chdir(r'/workspaces/PythonProgramming/file_handling_kachra') # for github codespace
os.chdir(r'C:\Users\hp\Desktop\PythonProgramming\file_handling_kachra') # for local vs code
# print(os.getcwd())










# CSV FILES

import csv 

"""
1. Writing into csv file using csv.Writer():
    a. using writerow([])
    b. using writerows([[], [], []])

2. Writing into csv file using csv.DictWriter():
    a. using writerow({key:value})
    b. using writerows([{}, {}, {}])

3. Reading from csv file:
    a. using csv.reader()
    b. using csv.dictreader()

"""








# writing into csv using csv.writer
"""
syntax:
with open('filename','mode',newline="") as file:
    var_name = csv.writer(fileName)
    var_name.writerow([])
    var_name.writerows([[], [], []])

"""

# with open('csv_dot_writer.csv', 'w', newline='') as file: # newline is used to avoid new line after each row
#     data = csv.writer(file)
#     data.writerow(['Rahul', 'Rushabh', 'Prabhu sir'])
#     data.writerow([500, 300, 999])
#     data.writerows(
#       [
#           ['apple',100,500],
#           ['Grapes',400,1000],
#           ['banana', 300,500]
#       ])
# os.popen('csv_dot_writer.csv') # if file already open, it gives PERMISSION ERROR







"""vvi"""

# writing into csv using csv.dictwriter
"""
syntax:

with open('filename','mode',newline="") as file:
    var_name = csv.DictWriter(iterator,[header1,header2,....])
    var_name.writeheader()
    var_name.writerow({'header1':"value"})
    var_name.writerows([{'header1':"value"},{'header1':"value"}])
"""

# with open('csv_dot_dictwriter.csv','w',newline='') as file: # newline is used to avoid new line after each row
#     x = csv.DictWriter(file, ['Sname', 'Branch'])
#     x.writeheader() # must use it to write column name
#     x.writerow({'Sname':"Rahul", 'Branch': 'EC'})
#     x.writerows([
#         {'Sname':"Aniket", 'Branch': 'ME'},
#         {'Sname':"Hitesh", 'Branch': 'CS'}
#         ])
# os.popen('csv_dot_dictwriter.csv') # if file already open, it gives PERMISSION ERROR












# READING DATA FROM CSV FILE

# 1. syntax: csv.reader()
"""
# with open('filename', 'mode') as file:
#     new_var = csv.reader(iterable)
#     print(new_var) ------> object address
#     print(list(new_var)) typecasting
#     for i in new_var:
#       print(i)  #looping
"""

# with open('csv_dot_writer.csv','r') as file:
#     data = csv.reader(file)
#     # print(data) #------> object address
#     # print(list(data)) #typecasting
#     for i in data:
#         print(i)  #looping



# 2. syntax: csv.DictReader()
"""
with open('filename','mode',newline="") as file:
#     new_var = csv.DictReader(iterable)
#     print(new_var) ------> object address
#     print(list(new_var)) typecasting
#     for i in data:
#       print(i)  #looping
"""

with open('csv_dot_dictwriter.csv','r') as file:
    data = csv.DictReader(file)
    # print(data) #------> object address
    print(list(data)) #typecasting
    # for i in data:
    #     print(i)  #looping