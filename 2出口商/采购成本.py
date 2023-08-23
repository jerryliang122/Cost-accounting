import os
import time
import math

cjsl = float(open('./cache/ck/cjsl.txt').read())
gcjg = float(open('./cache/ck/gcjg.txt').read())
ghjg = cjsl * gcjg
ts = float(open('./cache/ck/ts.txt').read())
zzs = float(open('./cache/ck/zzs.txt').read())
tssl = ghjg / (1+zzs) * ts
with open('./cache/ck/tssl.txt','w+') as file:
    file.write(str(tssl))
with open('./cache/ck/ghjg.txt','w+') as file:
    file.write(str(ghjg))
hj = ghjg - tssl
with open('./cache/ck/cgcbhj.txt','w+') as file:
    file.write(str(hj))