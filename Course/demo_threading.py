import time
import random
from threading import Thread

def myfunc(i):
    t = random.randint(3, 7)
    print(f"sleeping {t} sec from thread {i}")
    time.sleep(t)
    print(f"finished sleeping from thread {i}")

for i in range(10):
    t = Thread(target = myfunc, args = (i, ))
    t.start()
