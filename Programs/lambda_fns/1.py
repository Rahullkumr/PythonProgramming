# sum of two nos using fn

# def add(a,b):
#     return a+b 

# print(add(5,6))

# # sum of two nos using lambda

# add = lambda a,b: a+b 

# print(add(11,55))


# PROGRAMS

# 1.wap to find square and cube of given number
# find = lambda n: (n**2, n**3)
# print(find(11))


# 2.wap to check the given number is palindrome or not
# pali_or_not = lambda word: "palindrome" if  word == int(str(word)[::-1]) else 'Not Palindrome'
# print(pali_or_not(121))


# 3.wap to convert negative number to positive number
# conv = lambda n: n if n>0 else n*-1
# print(conv(-19))


# 4.wap to return the key of a dictionary

# a={"hello":"Sony","How":"are","you":"bye"}
# return_keys = lambda d: d.keys()
# print(return_keys(a))


# 5.wap to check if the number is even or odd
# even_odd = lambda n: 'odd' if n%2 == 1 else 'even'
# print(even_odd(34))
# print(even_odd(3))



# 6.wap which returns first element of a sequence
# return_first_element = lambda s: (s[0], s[-1]) if isinstance(s, (list, str, tuple)) else 'not a sequence'
# print(return_first_element([1,3,6]))
# print(return_first_element(765))
# print(return_first_element(('I', 'am','tupple')))



# 7.wap which returns length of any iterable
# return_len = lambda i: len(i) if isinstance(i, (list, str, tuple, set, dict)) else 'not an iterable'
# print(return_len([1,3,6]))
# print(return_len(765))
# print(return_len(('I', 'am','tupple')))


# 8.wap which returns the list of squares of numbers in a list

#l=[2,3,4,5,6]
#los = lambda l: [i**2 for i in l]
#print(los(l))



# 9.wap to check list elements are palindrome or not

# l=["nayana","kayak","mom","school","bag","dad"]
# check_pali = lambda l: [True if i == i[::-1] else False for i in l]
# print(check_pali(l))

# 10.wap to print the numbers present in a list with their corresponding indices pair

# l=[100,200,300,400,500]
# no_index_pair = lambda var: [(j,i) for i,j in enumerate(var)]
# print(no_index_pair(l))

# 11.wap to check a data is sequence if it is sequence then return length pair else type pair
jagah = lambda var: [(len(var), i) if isinstance(i, (list, str, tuple)) else (type(var), i) for i in var]
print(jagah(["hello",2,['a', '66'],4]))



# 12.wap to check given number is divisible by 5 and 3



# 13.wap to check even or odd,if it is even return square of that value else square root of that

# value



# 14.wap to check len of given string ,if length is even return as it is else return reverse

# of that string

# 15.wap to check length of given string and return value and length in tuple and dictionary
