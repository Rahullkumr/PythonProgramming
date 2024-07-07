#Nested For(Pattern Programming)
# for i in range(1,3):
#     for j in range(1,4):
#         print(i*j,end=" ")
#
a=int(input("Enter the Number of rows"))
for i in range(a):
    print("*")




#Steps:
"""
1) Controlling No of Rows
2) Controlling No of Columns
3) Empty Print(Outside Nested Loop)
"""
# Rectangle or Square Pattern
# a=int(input("Enter the Number of Rows: "))
# b=int(input("No of Columns: "))
# for i in range(a):
#     for j in range(b):
#         print("*",end=" ")
#   print()





# a=int(input("Enter the Number of Rows: "))   o/p:- 1111
# b=int(input("No of Columns: "))                    2222
# for i in range(1,a):
#     for j in range(b):
#         print(i,end=" ")
#     print()

# a=int(input("Enter the Number of Rows: ")) o/p: same as above
# b=int(input("No of Columns: "))
# val=1
# for i in range(1,a):
#     for j in range(1,b):
#         print(val,end="")
#     print()
#     val+=1


# a=int(input("Enter the Number of Rows: "))
# b=int(input("No of Columns: "))
# for i in range(a):
#     val = 1
#     for j in range(b):
#         print(val,end="")
#         val+=1
#     print()

"""o/p:12345
       12345
       12345"""


# a=int(input("Enter the Number of Rows: "))
# b=int(input("No of Columns: "))
# for i in range(a):
#     val = 1
#     for j in range(b):
#         print(val,end="")
#         val+=1
#         if (val>9):
#             val=1
#     print()

"""Op:
123456789123
123456789123
123456789123"""

# row=int(input("Enter the Number of Rows: "))
# col=int(input("No of Columns: "))
# val=row
# if val>9:
#     val=9
# for i in range(row):
#     for j in range(col):
#         print(val,end="")
#     print()
#     val-=1
#     if  val<1:
#         val=9

"""
Enter the Number of Rows: 11
No of Columns: 5
99999
88888
77777
66666
55555
44444
33333
22222
11111
99999
88888


"""

# row=int(input("Enter the Number of Rows: "))
# col=int(input("No of Columns: "))
# for i in range(row):
#     val=col
#     for j in range(col):
#         print(val,end=" ")
#         val-=1
#     print()



# row=int(input("Enter the Number of Rows: "))
# col=int(input("No of Columns: "))
# val=ord("A")
# for i in range(row):
#     for j in range(col):
#         print(chr(val),end=" ")
#     print()
#     val+=1

"""
Enter the Number of Rows: 4
No of Columns: 4
A A A A 
B B B B 
C C C C 
D D D D 



"""


# row=int(input("Enter the Number of Rows: "))
# col=int(input("No of Columns: "))
# val=ord("A")
# for i in range(row):
#     for j in range(col):
#         print(chr(val),end=" ")
#     print()
#     val+=1
#     if val>ord("Z"):
#         val=ord("A")
#
"""
Enter the Number of Rows: 27
No of Columns: 4
A A A A 
B B B B 
C C C C 
D D D D 
E E E E 
F F F F 
G G G G 
H H H H 
I I I I 
J J J J 
K K K K 
L L L L 
M M M M 
N N N N 
O O O O 
P P P P 
Q Q Q Q 
R R R R 
S S S S 
T T T T 
U U U U 
V V V V 
W W W W 
X X X X 
Y Y Y Y 
Z Z Z Z 
A A A A """

#
# row=int(input("Enter No of Rows"))
# col=int(input("Enter No of Columns"))
# for i in range(row):
#     val=ord("A")
#     for j in range(col):
#         print(chr(val),end=" ")
#         val+=1
#         if val>ord("Z"):
#             val=ord("A")
#     print()
"""
Enter No of Rows5
Enter No of Columns28
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z A B 
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z A B 
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z A B 
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z A B 
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z A B 
"""


"""
homework
1:
ccc
bbb
aaa

2:
cba
cba
cba
"""