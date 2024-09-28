import multiprocessing as mp

def job():
    print('Start ...')
    for i in range(1000000):
        2**2
    print('Done')

if(__name__=='__main__'):
    p = mp.Process(target=job)
    p.start()
    print('Process')
   

-----------------

def job(a,b):
    print(a+b)

if(__name__=='__main__'):
    p = mp.Process(target=job,args=(1,2))
    p.start()
   
-----------------

import time

def job(a,x):
    for i in range(5):
        x += 1
        time.sleep(0.5)
        print('%s=%d'%(a,x))

if(__name__=='__main__'):
    p1 = mp.Process(target=job,args=('x',1))
    p2 = mp.Process(target=job,args=('y',11))
    p1.start()
    p2.start()
    print('Done')



------------------------

def job(a):
    for i in range(1,4):
        time.sleep(0.5)
        print('Job %d Round %d'%(a,i))

if(__name__=='__main__'):
    for j in range(1,6):
        p = mp.Process(target=job,args=(j,))
        p.start()
    print('Done')
   
-----------------------------

def job(a):
    for i in range(2):
        time.sleep(0.5)
        print('Job %d Round %d'%(a,i))

if(__name__=='__main__'):
    pp = []
    for j in range(4):
        p = mp.Process(target=job,args=(j+1,))
        p.start()
        pp.append(p)
    print('Done')
    for p in pp:
        p.join()
    print('Sweep all jobs')
   
   
--------------------------------

def job(a):
    return a

if(__name__=='__main__'):
    p = mp.Process(target=job,args=(1,))
    a = p.start()
    print(a)
   
   
---------------------------------


def job(a,q):
    q.put(a**3)

if(__name__=='__main__'):
    q = mp.Queue()
    p = mp.Process(target=job,args=(2,q))
    p.start()
    a = q.get()
    print(a)
   
   
------------------------------------


def job(a,b,q):
    q.put(a*b)
    q.put(a**b)

if(__name__=='__main__'):
    q = mp.Queue()
    p = mp.Process(target=job,args=(2,3,q))
    p.start()
    print(q.get())
    print(q.get())
   
   
   
----------------------------------------

def job(s,ro,q):
    time.sleep(ro)
    q.put(s)

if(__name__=='__main__'):
    q = mp.Queue()
    p1 = mp.Process(target=job,args=('p1',3,q))
    p1.start()
    p2 = mp.Process(target=job,args=('p2',2,q))
    p2.start()
    print(q.get())
    print(q.get())