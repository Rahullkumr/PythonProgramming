a = [1, 2, 3, 4, 5, 6]
x = lambda i: i % 2 == 0
print(list(map(x, a)))
print(list(filter(x, a)))

# Q1
# names=["manu","lohit","jivago","wank","yaseen"]
# x=lambda i:i[0]
# print(list(map(x,names)))


# Q2
# names1=["laptop","mouse","board","house","week"]
# x=lambda i:[i,len(i)]
# print(list(map(x,names1)))

# Q3
# l1=[2,3,4,5,6]
# l2=[3,4,5,8,9]
# x=lambda a,b:a+b
# print(list(map(x,l1,l2)))


# Q4
# names=["a","b","c","d"]
# age=[20,35,21,56]
# x=lambda i:{names:age}
# print(list(map(x,names,age)))
# print(list(zip(names,age)))

# Q5
# d={10:"ten","hai":"value",(1,2,3):"colln",1.2:"decimal"}
#
# x=lambda i:d[i] if isinstance(i,(int,float,complex,bool)) else type(i)
# print(list(map(x,d)))
# # x=lambda i:d.values() if isinstance(d.keys(),(int,float,bool,complex))  else type(i)
# # print(list(map(x,d)))
