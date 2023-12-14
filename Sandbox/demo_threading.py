import time
from threading import Thread
from random import randint


def myfunc(i):
    t = randint(3, 7)
    print("sleeping %d sec from thread %d" % (t, i))
    time.sleep(t)
    print("finished sleeping from thread %d" % i)



for i in range(10):
    t = Thread(target=myfunc, args=(i,))
    t.start()
