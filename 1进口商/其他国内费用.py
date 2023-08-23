# -*- coding: utf-8 -*-
import os 
import math
import time 

cjj = open('./cache/jk/cjj.txt').read()
jyf = input('是否有检疫1有/2无:')

def jy():
    jyzd = 7.1
    jyfl = 0.08 / 100
    jyf = float(cjj) * jyfl
    jy = max(jyf,jyfl)
    print(jy)
    with open('./cache/jk/jyfy.txt',"a+") as file:
        file.write(str(jy))
    return jy
def bgf():
    bgf = 11.83
    with open('./cache/jk/bgf.txt','a+') as file:
        file.write(str(bgf))
    return bgf
def hdzf():
    zfl = 0.25 / 100 * float(cjj)
    zfzd = 59.14
    zf = max(zfl,zfzd)
    print(zf)
    with open('./cache/jk/hdzf.txt','a+') as file:
        file.write(str(zf))
    return zf
if jyf == '1':
    jyy = jy()
else:
    jyy = float(0)
    with open('./cache/jk/jyfy.txt',"a+") as file:
        file.write(str(jyy))
bgff = bgf()
hdzff = hdzf()
hj = jyy + bgff + hdzff
print(hj)
with open('./cache/jk/gnfyhy.txt',"a+") as file:
    file.write(str(hj))