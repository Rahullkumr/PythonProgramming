# if you want to set a thread as daemon, set it before starting it else
# it will give runtime error,  we can't set active thread as daemon

# use of daemon: for supporting main thread


from threading import *
import time

print(current_thread().isDaemon())
# print(current_thread().setDaemon(True))
current_thread().setDaemon(True)


# def Test(name):
#     for i in range(5):
#         print('good afternoon')
#         time.sleep(2)
#         print(name)
# t = Thread(target=Test, args=('Ravi'))
# t1 = Thread(target=Test, args=('Virat'))
# t.start()
# t1.start()

# SYNCHRONIZATION
"""
3 fns:
    1. lock     ==> used to hold the thread by using acquire(), and release using release()
    2. rlock
    3. semaphore
"""

l = Lock()

def Test(name):
    l.acquire()
    for i in range(5):
        print('good afternoon')
        print(name)
    l.release()
t = Thread(target=Test, args=("Ravi",))
t1 = Thread(target=Test, args=("Virat",))
t.start()
t1.start()



























