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
zcb = float(gnfyhj) + float(cgcbhj) + yfbxf
yke = float(dwbj) - float(zcb)
ykv = yke / zcb * 100
file = open('./cache/ck/ykv.txt','w+')
file.write(str(ykv))
file.close()
file = open('./cache/ck/yke.txt','w+')
file.write(str(yke))
file.close()