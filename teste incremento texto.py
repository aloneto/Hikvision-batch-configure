import threading
from datetime import datetime,timedelta
import time

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

now = datetime.now()
fim = now + timedelta(seconds=2)
print(now)
print(fim)
ok =True
while ok is True:

    now = datetime.now()
    if now > fim:
        ok = False



    print ("fim")




def incrementa(msg):
    for i in reversed(range(6)):
        datastart=datetime.datetime.now()
        lista[i] = lista[i - 1]
        time.sleep(0.1)

        while datastart < datetime.datetime.now():
            pass


    lista[0] = msg
    print(lista)


while newmsg ==True:
    pass

t = threading.Thread(target=incrementa, args=(msgnova1,))
t.start()
while t.isAlive():
    print("Aguardando thread")
    time.sleep(0.1)
print("Thread morreu")

contador =0

def timer(contador):
    while contador < 5:
        print (contador,"tentativa")
        contador +=1

        time.sleep(0.5)
    print ("finalizado")

timer(0)



incrementa(msgnova1)
incrementa(msgnova2)
incrementa(msgnova3)
time.sleep(10)
for i in range(0,6):
    incrementa("")



















