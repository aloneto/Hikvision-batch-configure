import time

def foo(bar, baz):
  print ('hello {0}'.format(bar))
  return 'foo' + baz

from multiprocessing.pool import ThreadPool
pool = ThreadPool(processes=1)

async_result = pool.apply_async(foo, ('world', 'foo')) # tuple of args for foo
time.sleep(5)

# do some other stuff in the main process

return_val = async_result.get()  # get the return value from your function.
print (return_val)

import threading
import time


def worker(message):
    for i in range(5):
        print
        message
        time.sleep(1)

'''
t = threading.Thread(target=worker, args=("thread sendo executada",))
t.start()
while t.isAlive():
    print
    "Aguardando thread"
    time.sleep(5)

print
"Thread morreu"
print
"Finalizando programa"
'''