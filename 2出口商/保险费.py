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
        bxf = 0.0088 * bxje
        print(bxf)
        with open('./cache/ck/bxf.txt','w+') as file1:
            file1.write(str(bxf))
        with open('./cache/ck/bxje.txt','w+') as file1:
            file1.write(str(bxje))
    elif mysy == "2":
        bxf = float(htje) * 0.00977
        print(bxf)
        with open('./cache/ck/bxf.txt','w+') as file1:
            file1.write(str(bxf))
        bxje = float(htje) * 1.1
        with open('./cache/ck/bxje.txt','w+') as file1:
            file1.write(str(bxje))
    else:
        with open('./cache/ck/bxf.txt','w+') as file1:
            file1.write(str(0))
        with open('./cache/ck/bxje.txt','w+') as file1:
            file1.write(str(0))

def kongyun():
    if mysy == '3':
        bxje=float(htje) * 1.1
        bxf = 0.0088 * bxje
        print(bxf)
        with open('./cache/ck/bxf.txt','w+') as file1:
            file1.write(str(bxf))
    elif mysy == "2":
        bxf = float(htje) * 0.0047
        print(bxf)
        with open('./cache/ck/bxf.txt','w+') as file1:
            file1.write(str(bxf))
        bxje = float(htje) * 1.1
    else:
        with open('./cache/ck/bxf.txt','w+') as file1:
            file1.write(str(0))
        bxje = float(0) * 1.1
    with open('./cache/ck/bxje.txt','w+') as file1:
        file1.write(str(bxje))
if ysfs == "1":
    haiyun()
else:
    kongyun()