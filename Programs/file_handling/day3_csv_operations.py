import os
print(os.getcwd())

os.chdir(r'/workspaces/PythonProgramming/file_handling_kachra') 
# print(os.getcwd())

# CSV FILES

import csv 

# writing into csv using csv.writer

# with open('laptop.csv', 'w', newline='') as file:
#     data = csv.writer(file)
#     data.writerow(['Rahul', 'Rushabh', 'Prabhu sir'])
#     data.writerow([100, 300, 999])

# with open('laptop.csv', 'a', newline='') as file:
#     data = csv.writer(file)
#     data.writerows([['apple',100,500],['Grapes',400,1000],['banana', 300,500]])

# os.popen('laptop.csv')



"""vvi"""
# writing into csv using csv.dictwriter

# with open('mobile.csv','w',newline='') as file:
#     x = csv.DictWriter(file, ['Sname', 'Branch'])
#     x.writeheader() # must use it
#     x.writerow({'Sname':"Rahul", 'Branch': 'EC'})

# os.popen('mobile.csv')

"""
with open('filename','mode',newline="") as file:
    var_name = csv.DictWriter(iterator,[header1,header2,....])
    var_name.writeheader()
    var_name.writerow({'header1':"value"})
    var_name.writerows([{'header1':"value"},{'header1':"value"}])

"""
# with open('mobile.csv','w',newline='') as file:
#     x = csv.DictWriter(file, ['Sname', 'Branch'])
#     x.writeheader() # must use it
#     x.writerows([
#         {'Sname':"Rahul", 'Branch': 'EC'},
#         {'Sname':"Hitesh", 'Branch': 'CS'}
#         ])

# READING DATA FROM CSV FILE

# syntax: csv.reader
"""
# with open('filename', 'mode') as file:
#     new_var = csv.reader(iterable)
#     print(new_var) ------> object address
#     print(list(new_var)) typecasting
#     for i in data:
#       print(i)  #looping
"""


# syntax: csv.dictreader
"""
with open('filename','mode',newline="") as file:
    kar lo complete
"""