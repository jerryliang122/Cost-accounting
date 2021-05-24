# -*- coding: utf-8 -*-
import os
import math
import time

mysy = open('./cache/jk/mysy.txt').read()
htje = open('./cache/jk/cjj.txt').read()
ysfs = open('./cache/jk/ysfs.txt').read()
def haiyun():
    if mysy == '1':
        yf = open('./cache/jk/yf.txt').read()
        htjg = float(htje)+float(yf)
        bxf = float(htjg) * 0.00977
        print(str(bxf))
        file1 =open('./cache/jk/bxf.txt','a+')
        file1.write(str(bxf))
        file1.close()
        file1 =open('./cache/jk/bxje.txt','a+')
        file1.write(str(htjg))
        file1.close()
        pass
    elif mysy =="2":
        bxf = float(htje) * 0.00977
        print(str(bxf))
        file1 =open('./cache/jk/bxf.txt','a+')
        file1.write(str(bxf))
        file1.close()
        file1 =open('./cache/jk/bxje.txt','a+')
        file1.write(str(htje))
        file1.close()
        pass
    else:
        bxje=float(htje) * 1.1
        bxf = float(0.0088) * bxje
        print(str(bxf))
        file1 =open('./cache/jk/bxf.txt','a+')
        file1.write(str(bxf))
        file1.close()
        file1 =open('./cache/jk/bxje.txt','a+')
        file1.write(str(bxje))
        file1.close()

def kongyun():
    if mysy == '1':
        yf = open('./cache/jk/yf.txt').read()
        htjg = float(htje)+float(yf)
        bxf = float(htjg) * 0.0047
        print(str(bxf))
        file1 =open('./cache/jk/bxf.txt','a+')
        file1.write(str(bxf))
        file1.close()
        pass
    elif mysy =="2":
        bxf = float(htje) * 0.0047
        print(str(bxf))
        file1 =open('./cache/jk/bxf.txt','a+')
        file1.write(str(bxf))
        file1.close()
        pass
    else:
        bxje=float(htje) * 1.1
        bxf = float(0.0088) * bxje
        print(str(bxf))
        file1 =open('./cache/jk/bxf.txt','a+')
        file1.write(str(bxf))
        file1.close()
if ysfs == "1":
    haiyun()
else:
    kongyun()