import threading
import time
from concurrent.futures import ThreadPoolExecutor

def func(sec):
    print (f"sleeping for {sec} seconds")
    time.sleep(sec)

def main():

    time1=time.perf_counter()
    func(3)
    func(2)
    func(1)
    time2=time.perf_counter()
    print(time2-time1)

    time1=time.perf_counter()
    t1=threading.Thread(target=func,args=[3])
    t2=threading.Thread(target=func,args=[2])
    t3=threading.Thread(target=func,args=[1])

    t1.start()
    t2.start()# program running in bg
    t3.start()

    t1.join()
    t2.join()# to wait
    t3.join()

    time2=time.perf_counter()
    print(time2-time1)

def poolingDemo():
    with ThreadPoolExecutor() as executar:
        # f1=executar.submit(func,3)
        # f2=executar.submit(func,2)
        # f3=executar.submit(func,4)
        # print(f1.result())
        # print(f2.result())
        # print(f3.result())
        l=[3,4,1,5]
        results=executar.map(func,l)
        for result in results:
            print(result)


poolingDemo()