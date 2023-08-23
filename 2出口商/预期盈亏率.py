import os
import math
import time 
dwbj = open('./cache/ck/dwbj.txt').read()
mysy = open('./cache/ck/mysy.txt').read()
gnfyhj = open('./cache/ck/gnfyhj.txt').read()
cgcbhj = open('./cache/ck/cgcbhj.txt').read()
def yf():
    if mysy == '1':
        return float(0)
    elif mysy == '2':
        yf = open('./cache/ck/yf.txt').read()
        return float(yf)
    else:
        yf = open('./cache/ck/yf.txt').read()
        bxf = open('./cache/ck/bxf.txt').read()
        return float(yf) + float(bxf)
#运费保险费合集
yfbxf = yf()
zcb = float(gnfyhj) + float(cgcbhj) + yfbxf
yke = float(dwbj) - float(zcb)
ykv = yke / zcb * 100
with open('./cache/ck/ykv.txt','w+') as file:
    file.write(str(ykv))
with open('./cache/ck/yke.txt','w+') as file:
    file.write(str(yke))