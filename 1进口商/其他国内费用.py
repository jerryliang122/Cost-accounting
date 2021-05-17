# -*- coding: utf-8 -*-
import os 
import math
import time 

cjj = open('./cache/jk/cjj.txt').read()

def jy():
    jyzd = float(7.1)
    jyfl = float(0.08) / 100
    jyf = float(cjj) * jyfl
    jy = max(jyf,jyfl)
    print(str(jy))
    file = open('./cache/jk/jyfy.txt',"a+")
    file.write(str(jy))
    file.close()
    return jy
def bgf():
    bgf = float(11.83)
    file = open('./cache/jk/bgf.txt','a+')
    file.write(str(bgf))
    file.close()
    return bgf
def hdzf():
    zfl = float(0.25) / 100
    zfzd = float(59.14)
    zf = max(zfl,zfzd) 
    print(str(zf))
    file = open('./cache/jk/hdzf.txt','a+')
    file.write(str(zf))
    file.close()
    return zf

jyy = jy()
bgff = bgf()
hdzff = hdzf()
hj = jyy + bgff + hdzff
print(str(hj))
file = open('./cache/jk/gnfyhy.txt',"a+")
file.write(str(hj))
file.close()