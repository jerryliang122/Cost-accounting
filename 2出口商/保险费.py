# -*- coding: utf-8 -*-
import os
import math
import time

mysy = open('./cache/ck/mysy.txt').read()
htje = open('./cache/ck/dwbj.txt').read()
ysfs = open('./cache/ck/ysfs.txt').read()
def haiyun():
    if mysy == '3':
        bxje=float(htje) * 1.1
        bxf = float(0.0088) * bxje
        print(str(bxf))
        file1 =open('./cache/ck/bxf.txt','w+')
        file1.write(str(bxf))
        file1.close()
        file1 =open('./cache/ck/bxje.txt','w+')
        file1.write(str(bxje))
        file1.close()
        pass
    elif mysy =="2":
        bxf = float(htje) * 0.00977
        print(str(bxf))
        file1 =open('./cache/ck/bxf.txt','w+')
        file1.write(str(bxf))
        file1.close()
        bxje = float(htje) * 1.1
        file1 =open('./cache/ck/bxje.txt','w+')
        file1.write(str(bxje))
        file1.close()
        pass
    else:
        file1 =open('./cache/ck/bxf.txt','w+')
        file1.write(str(0))
        file1.close()
        file1 =open('./cache/ck/bxje.txt','w+')
        file1.write(str(0))
        file1.close()
        pass

def kongyun():
    if mysy == '3':
        bxje=float(htje) * 1.1
        bxf = float(0.0088) * bxje
        print(str(bxf))
        file1 =open('./cache/ck/bxf.txt','w+')
        file1.write(str(bxf))
        file1.close()
        file1 =open('./cache/ck/bxje.txt','w+')
        file1.write(str(bxje))
        file1.close()
        pass
    elif mysy =="2":
        bxf = float(htje) * 0.0047
        print(str(bxf))
        file1 =open('./cache/ck/bxf.txt','w+')
        file1.write(str(bxf))
        file1.close()
        bxje = float(htje) * 1.1
        file1 =open('./cache/ck/bxje.txt','w+')
        file1.write(str(bxje))
        file1.close()
        pass
    else:
        file1 =open('./cache/ck/bxf.txt','w+')
        file1.write(str(0))
        file1.close()
        bxje = float(0) * 1.1
        file1 =open('./cache/ck/bxje.txt','w+')
        file1.write(str(bxje))
        file1.close()
        pass
if ysfs == "1":
    haiyun()
else:
    kongyun()