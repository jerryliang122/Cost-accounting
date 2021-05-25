import os
import time
import math

cjsl = float(open('./cache/ck/cjsl.txt').read())
gcjg = float(open('./cache/ck/gcjg.txt').read())
ghjg = cjsl * gcjg
ts = float(open('./cache/ck/ts.txt').read())
tssl = ghjg * ts
file = open('./cache/ck/tssl.txt','a+')
file.write(str(tssl))
file.close()
file = open('./cache/ck/ghjg.txt','a+')
file.write(str(ghjg))
file.close()
hj = ghjg - tssl 
file = open('./cache/ck/cgcbhj.txt','a+')
file.write(str(hj))
file.close()