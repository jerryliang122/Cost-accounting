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
    pass
def bgf():
    pass
def hdzf():
    pass