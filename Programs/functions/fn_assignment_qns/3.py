# 3.wap to return length of variable keywords arguments

def variable_key_arg(**names):
    print(len(names))
variable_key_arg(v1 = 'Hello world', v2 = '"Python"')