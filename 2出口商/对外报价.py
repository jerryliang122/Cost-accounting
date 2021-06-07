import os
import math
import time

sl = open('./cache/ck/cjsl.txt').read()#数量
dj = open('./cache/ck/dj.txt').read()#单价
hj = float(sl) * float(dj)
file =open('./cache/ck/dwbj.txt','w+')
file.write(str(hj))
file.close()
