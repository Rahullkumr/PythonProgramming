# 12.write a function to print the below output
# func("TRACXN",1)
# #should print RCN
def func(s, si):
    output = s[si::2]
    return output

print(func("TRACXN",1))