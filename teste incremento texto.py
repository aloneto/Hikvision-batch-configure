import threading
from datetime import datetime, timedelta
import time

import threading


msgnova1 = 'novamsg1'
msgnova2 = 'novamsg2'
msgnova3 = 'novamsg3'
msgnova4 = 'novamsg4'
msgnova5 = 'novamsg5'
msgnova6 = 'novamsg6'
ln1 = 'msg1'
ln2 = 'msg2'
ln3 = 'msg3'
ln4 = 'msg4'
ln5 = 'msg5'
ln6 = 'msg6'
lista = [ln1, ln2, ln3, ln4, ln5, ln6]
newmsg = False

dateStart = None


def incrementa(msg):
    global dateStart
    dateStart = datetime.now()
    print("iniciado em: ", dateStart)
    for i in reversed(range(6)):
        lista[i] = lista[i - 1]
        time.sleep(0.1)
    lista[0] = msg
    time.sleep(1)
    if msg != " ":
        t = threading.Thread(target=timer, args=(0,))
        t.start()
        print("thead iniciada")


def timer(contador):
    global dateStart
    print("iniciado timer em: ", dateStart)
    for x in range(0, 5):
        print("contando tempo")
        time.sleep(1)
    dateEnd = datetime.now()
    if dateEnd > dateStart + timedelta(seconds=5):
        for i in range(0, 5):
            incrementa(" ")
            print("envia clear!!!!")


incrementa(msgnova1)
time.sleep(3)
incrementa(msgnova1)
time.sleep(3)
incrementa(msgnova1)
time.sleep(10)
