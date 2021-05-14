# -*- coding: utf-8 -*-
import os 
import math
import time 

cjj = open('./cache/jk/cjj.txt').read

def jy():
    jyzd = float(input('检疫最低手续费:'))
    jyfl = float(input('检疫费率:')) / 100
    jyf = cjj * jyfl
    jy = max(jyf,jyfl)
    print(str(jy))
    file = open('./cache/jk/jyfy.txt',"a+")
    file.write(str(jy))
    file.close()
    return jy
def bgf():
    bgf = float(input('报关费：'))
    file = open('./cache/jk/bgf.txt','a+')
    file.write(str(bgf))
    file.close()
    return bgf
def hdzf():
    zfl = float(input('杂费率:')) / 100
    zfzd = float(input('最低杂费:'))
    zf = max(zfl,zfzd) 
    print(str(zf))
    file = open('./cache/jk/hdzf.txt','a+')
    file.write(str(zf))
    file.close()
    return zf