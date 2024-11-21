'''day 4'''


"""
import time
from threading import *
l = Lock()
def spam(name):
    l.acquire()
    for i in range(3):
        print(i)
        time.sleep(2)
        print(name)
    l.release()
t = Thread(target=spam, args=('python', ))
t1 = Thread(target=spam, args=('web-tech', ))
t.start()
t1.start()
"""

# disadvantage of lock
# - we can't create multiple locks for single function/thread
# solution is:
    # RLock = raintraint lock
    # - we can lock a single thread many times

"""
from threading import *

r = RLock()
print('lock sys one')
r.acquire()
print('lock sys two')
r.acquire()
print('lock sys three')
r.release()
r.release()
"""

# how to run more than one threads simultaneously
# using SEMAPHORE()

# """
import time
from threading import *
s = Semaphore(2)        # number of threads to execute simultaneously
def spam(name):
    s.acquire()
    for i in range(3):
        print(i)
        time.sleep(2)
        print(name)
    s.release()
t = Thread(target=spam, args=('python', ))
t1 = Thread(target=spam, args=('web-tech', ))
t2 = Thread(target=spam, args=('Java', ))
t3 = Thread(target=spam, args=('Selenium', ))
t4 = Thread(target=spam, args=('CPP', ))
t.start()
t1.start()
t2.start()
t3.start()
t4.start()
# """





























