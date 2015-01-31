#!/usr/bin/env python

import time
import threading
import multiprocessing

class nothread(object):
    def foo(self):
        start=time.time()
        b=[]
        for i in range(1000000):
            b.append(i*i)
        print type(self),"Timing",str(time.time()-start)+'s'

class threaded(nothread):
    def foo(self):
        t=threading.Thread(target=super(threaded,self).foo)
        t.start()
        start=time.time()
        t.join()
        print type(self),"Joined after ",str(time.time()-start)+'s'

class twothreaded(nothread):
    def foo(self):
        t=threading.Thread(target=super(twothreaded,self).foo)
        t.start()
        start=time.time()
        a=[]
        for i in range(1000000):
            a.append(i*i)
        t.join()
        print type(self),"Joined after ",str(time.time()-start)+'s'

class sleepthread(nothread):
    def foo(self):
        def thread():
            start=time.time()
            for i in range(10):
                time.sleep(0.1)
            print "Slept for ",str(time.time()-start)+'s'
        t=threading.Thread(target=thread)
        t.start()
        super(sleepthread,self).foo()

class queuethread(nothread):
    def foo(self):
        def thread(q):
            q.get()
        q=multiprocessing.Queue()
        t=threading.Thread(target=thread,args=[q])
        t.start()
        super(queuethread,self).foo()
        q.put(1)
            

nothread().foo()
threaded().foo()
twothreaded().foo()
sleepthread().foo()
queuethread().foo()
