"""
13.write a function to print the below output
func("TRACXN",0)
#should print TAX
"""
def func(s, si):
    output = s[si::2]
    return output

print(func("TRACXN",0))