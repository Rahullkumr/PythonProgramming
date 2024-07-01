'''
14. A function take variable number of positional arguments as input. how to check if the arguments are more than 5.
'''
def check_len(*args):
    if len(args) > 5:
        print("more than 5 arguments")
check_len(1,2,3,4,5,6)