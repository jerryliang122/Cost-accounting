import os
import math
import time 
dwbj = open('./cache/ck/dwbj.txt').read()
mysy = open('./cache/ck/mysy.txt').read()
gnfyhj = open('./cache/ck/gnfyhj.txt').read()
cgcbhj = open('./cache/ck/cgcbhj.txt').read()
def yf():
    if mysy == '1':
        pass
        hj =float(0)
    elif mysy == '2':
        yf = open('./cache/ck/yf.txt').read()
        hj = float(yf)
    else:
        yf = open('./cache/ck/yf.txt').read()
        bxf = open('./cache/ck/bxf.txt').read()
        hj = float(yf) + float(bxf)
    return hj
#运费保险费合集
yfbxf = yf()
