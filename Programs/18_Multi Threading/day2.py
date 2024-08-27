from threading import *
import time

"""
def demo():
    print(current_thread().getName(),'thread started')
    time.sleep(3)
    print(current_thread().getName(),'thread ended')

print('active thread count', active_count())
t1 = Thread(target=demo, name='childThread1')
# t2 = Thread(target=demo, name='Child thread 2')
t1.start()
# t2.start()

print('active thread count number: ', active_count())
time.sleep(3)
print('active thread count number: ', active_count())
"""

# active_count()
"""
def spam():
    print(current_thread().name, 'start')
    time.sleep(2)
    print(current_thread().name, 'ended')

print('active thread count: ', active_count())
a = Thread(target=spam, name='thread_ka_naam ')
a.start()
print('active thread count: ', active_count())
time.sleep(3)
print('active count: ', active_count())
"""

# apply isalive()
"""
def spam():
    print(current_thread().name, 'start')
    # time.sleep(2)
    print(current_thread().name, 'ended')

print('active thread count: ', active_count())
t1 = Thread(target=spam, name='thread1 ')
t1.start()
t2 = Thread(target=spam, name='thread2 ')
t2.start()
print(f'is {t1.name} still alive? ', t1.is_alive())
print(f'is {t2.name} still alive? ', t2.is_alive())
# time.sleep(3)
print(f'After sleep, is {t1.name} still alive? ', t1.is_alive())
print(f'After sleep, is {t2.name} still alive? ', t2.is_alive())
"""

#

def func():
    for i in range(4):
        print('hello python')
        time.sleep(1)

x = Thread(target=func)
x.start()
x.join()    # if you want to get sequential output
for i in range(4):
    print('hell java')

# daemon threads

# - the threads which are running in the background are called daemon threads
# - the main objective of daemon thread is to provide support for non daemon threads(Main thread)
# - eg: garbage collector
# - whenever main thread runs with low memory, immediately PVM runs garbage collector
# to destroy useless objects and to provide free memory so that main thread can continue its execution without
# having any memory problems
# - we can check whether thread is daemon or not by using isDaemon() of thread class or using daemon property

print(current_thread().isDaemon())


















