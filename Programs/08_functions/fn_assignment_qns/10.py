# 10.wap to check the given characters is alphabets or digit or special characters

def print_my_type(ch):
    if ch.isalpha():
        print(f"{ch} is albhabet")
    elif ch.isdigit():
        print(f"{ch} is digit")
    else:
        print(f"{ch} is special character")
ch = '8'
if len(ch) == 1:
    print_my_type(ch)