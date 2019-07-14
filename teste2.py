import time


from multiprocessing.pool import ThreadPool
pool = ThreadPool(processes=1)



contador_is_running = True



def conta_tempo(sec):
    global contador_is_running
    contador_is_running = True
    for x in range (1,5):
        print ("contando tempo")
        time.sleep(1)
    print ("fim")
    contador_is_running = False
    return  contador_is_running


async_result = pool.apply_async(conta_tempo, (5,)) # tuple of args for foo
print ("teste")


conta_tempo(10)


return_val = async_result.get()  # get the return value from your function.
print ("contador tempo ",return_val)

