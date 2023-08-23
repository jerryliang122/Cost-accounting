import os
import math
import time

sl = open('./cache/ck/cjsl.txt').read()#数量
dj = open('./cache/ck/dj.txt').read()#单价
hj = float(sl) * float(dj)
with open('./cache/ck/dwbj.txt','w+') as file:
    file.write(str(hj))
