import os
import math
import time


#产地证书费用
cdzsf = float(0)
with open('./cache/ck/cdzsf.txt','w+') as file:
    file.write(str(cdzsf))
ckjy = open('./cache/ck/ckjy.txt').read()
if ckjy == '1':
    #检疫费用
    jy = 0.08 / 100
    jyzd = 7.1
    jyfy = max(jy,jyzd)
    file = open('./cache/ck/jyfy.txt','w+')
    file.write(str(jyfy))
else:
    file = open('./cache/ck/jyfy.txt','w+')
    file.write(str(0))
    jyfy = 0
file.close()
with open('./cache/ck/jyzsf.txt','w+') as file:
    file.write(str(0))#检疫证书费用，待填写
#报关费
bgf = float(0)
with open('./cache/ck/bgf.txt','w+') as file:
    file.write(str(bgf))
#出口货代杂费
ckhdzfl = 0.25 / 100
ckhdzfmin = 59.14
ckhdzf = max(ckhdzfl,ckhdzfmin)
with open('./cache/ck/ckhdzf.txt','w+') as file:
    file.write(str(ckhdzf))
#银行费用
yhfy = 1.77
with open('./cache/ck/yhfy.txt','w+') as file:
    file.write(str(yhfy))
#其他费用

#国内费用合集
gnfyhj = cdzsf + jyfy + bgf + yhfy
with open('./cache/ck/gnfyhj.txt','w+') as file:
    file.write(str(gnfyhj))
