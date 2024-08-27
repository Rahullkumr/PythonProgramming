import threading

""""
Multitasking
    1. Process based
    2. Thread based
"""

# print(threading.current_thread())   # <_MainThread(MainThread, started 17732)>
# # pvm creates _MainThread
#
# print(threading.current_thread().name)
# print(threading.current_thread().ident)     # thread id
#
# threading.current_thread().setName('python')
# print(threading.current_thread().getName())


# how to create a thread
from threading import *
# class Mainclass(Thread):
#     def run(self):
#         for i in range(4):
#             print('python class')
#             print(threading.current_thread())

# t = Mainclass()
# t.start()

# for i in range(4):
#     print('webtech class')
#     print(threading.current_thread())
#
# def mainfn():
#     print('main fn')
#     print(threading.current_thread())
#
# mainfn()


#
def spam(n, **kwargs):
    for i in range(n):
        print(threading.current_thread())
        print(i, kwargs)

t = Thread(target=spam, kwargs={'1':'hello'}, args=(4,))
t.start()

