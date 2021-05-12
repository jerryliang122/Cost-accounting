# -*- coding: utf-8 -*-
import os
import math
import time

mysy = open('./cache/jk/mysy.txt','a+').read()
htje = open('./cache/jk/cjj.txt','a+').read()

def haiyun():
    if mysy == '1':
        yf = open('./cache/jk/yf.txt','a+').read()
        
        pass
    elif mysy =="2":
        bxf = float(htje) * 1.1 / 0.99032
        file1 =open('./cache/jk/bxf.txt','a+')
        file1.write(str(bxf))
        file1.close()
        pass
    else:
        bxje=float(htje) * 1.1
        bxf = float(0.0088) * bxje
        file1 =open('./cache/jk/bxf.txt','a+')
        file1.write(str(bxf))
        file1.close()

def kongyun():
    pass