
# 2.wap to check string is palindrome or not (take user input)

def palin(s):
    if s == s[::-1]:
        return 'Palindrome'
    else:
        return 'Not Palindrome'

s = input("enter any word: ")
print(palin(s))