import os
import math
import time

sl = open('./cache/ck/cjsl.txt').read()
dj = open('./cache/ck/dj.txt').read()
hj = float(sl) * float(dj)
file =open('./cache/ck/dwbj.txt','w+')
file.write(str(hj))
file.close()