#!/usr/bin/python
# -*- coding:utf-8 -*-

from daccont import *
from AIO import *
import threading

def ret_main():
    try:
        while(1):
            main()
            time.sleep(1)
    except :
        exit()


thread1 = threading.Thread(target=dac_control,daemon=True)
thread2 = threading.Thread(target=ret_main,daemon=True)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Program end     ")
