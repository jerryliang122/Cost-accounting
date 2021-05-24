# -*- coding: utf-8 -*-
import os
import time
import math
jksfhj = float(open('./cache/jk/jksfhj.txt').read())
yhfyhj = float(open('./cache/jk/yhfyhj.txt').read())
qtgnfyhj = float(open('./cache/jk/gnfyhy.txt').read())
cif = float(open('./cache/jk/cif.txt').read())
yfhj = float(open('./cache/jk/yf.txt').read())
bxfhj = float(open('./cache/jk/bxf.txt').read())
zcb = cif + qtgnfyhj + yhfyhj + jksfhj + yfhj + bxfhj
xhsl = float(open('./cache/jk/xhsl.txt').read())
yqyke = xhsl - zcb
ykl = yqyke / zcb * 100
file = open('./cache/jk/yqyke.txt','a+')
file.write(str(yqyke))
file.close()
file1 = open('./cache/jk/ykl.txt',"a+")
file1.write(str(ykl))
file1.close()