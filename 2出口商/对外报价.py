import os
import math
import time

sl = open('./cache/ck/sl.txt').read()
dj = open('./cache/ck/dj.txt').read()
hj = float(sl) * float(dj)
file =open('./cache/ck/dwbj.txt','W+')
file.write(str(hj))
file.close()