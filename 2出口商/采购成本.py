import os
import time
import math

cjsl = float(open('./cache/ck/cjsl.txt').read())
gcjg = float(open('./cache/ck/gcjg.txt').read())
ghjg = cjsl * gcjg
ts = float(open('./cache/ck/ts.txt').read())
zzs = float(open('./cache/ck/zzs.txt').read())
tssl = ghjg / (1+zzs) *ts
file = open('./cache/ck/tssl.txt','w+')
file.write(str(tssl))
file.close()
file = open('./cache/ck/ghjg.txt','w+')
file.write(str(ghjg))
file.close()
hj = ghjg - tssl 
file = open('./cache/ck/cgcbhj.txt','w+')
file.write(str(hj))
file.close()