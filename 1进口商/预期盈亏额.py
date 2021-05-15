# -*- coding: utf-8 -*-
import os
import time
import math
jksfhj = float(open('./cache/jk/jksfhj.txt').read())
yhfyhj = float(open('./cache/jk/yhfyhj.txt').read())
qtgnfyhj = float(open('./cache/jk/gnfyhy.txt').read())
cif = float(open('./cache/jk/cif.txt').read())
zcb = cif + qtgnfyhj + yhfyhj + jksfhj
xhsl = float(open('./cache/jk/xhsl.txt').read())
yqyke = zcb - xhsl
ykl = xhsl / zcb
file = open('./cache/jk/yqyke.txt','a+')
file.write(yqyke)
file.close()
file1 = open('./cache/jk/ykl.txt',"a+")
file1.write(ykl)
file1.close()