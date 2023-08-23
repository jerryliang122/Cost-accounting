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
        print(bxf)
        with open('./cache/jk/bxf.txt','a+') as file1:
            file1.write(str(bxf))
        bxje = htjg * 1.1
        file =open('./cache/jk/bxje.txt','a+')
        print(bxje)
    elif mysy == "2":
        bxf = float(htje) * 0.00977
        print(bxf)
        with open('./cache/jk/bxf.txt','a+') as file1:
            file1.write(str(bxf))
        bxje = float(htje) * 1.1
        file =open('./cache/jk/bxje.txt','a+')
    else:
        bxje=float(htje) * 1.1
        bxf = 0.0088 * bxje
        print(bxf)
        with open('./cache/jk/bxf.txt','a+') as file1:
            file1.write(str(bxf))
        file =open('./cache/jk/bxje.txt','a+')
    file.write(str(bxje))
    file.close()

def kongyun():
    if mysy == '1':
        yf = open('./cache/jk/yf.txt').read()
        htjg = float(htje)+float(yf)
        bxf = float(htjg) * 0.0047
        print(bxf)
        with open('./cache/jk/bxf.txt','a+') as file1:
            file1.write(str(bxf))
        file =open('./cache/jk/bxje.txt','a+')
        file.write(str(htjg))
    elif mysy == "2":
        bxf = float(htje) * 0.0047
        print(bxf)
        with open('./cache/jk/bxf.txt','a+') as file1:
            file1.write(str(bxf))
        file =open('./cache/jk/bxje.txt','a+')
        file.write(str(htje))
    else:
        bxje=float(htje) * 1.1
        bxf = 0.0088 * bxje
        print(bxf)
        file =open('./cache/jk/bxje.txt','a+')
        file.write(str(bxf))
    file.close()
if ysfs in ["集装箱", '散货']:
    haiyun()
else:
    kongyun()
