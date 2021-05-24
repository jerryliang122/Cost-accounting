import os
import time
import math

cjsl = float(input('成交数量:'))
gcjg = float(input('工厂价格:'))
ghjg = cjsl * gcjg
ts = float(input('退税率:')) / 100
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