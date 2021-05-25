import os
import math
import time


#产地证书费用
cdzsf = float(0)
file = open('./cache/ck/cdzsf.txt','w+')
file.write(str(cdzsf))
file.close()
ckjy = open('./cache/ck/ckjy.txt').read()
if ckjy == '1':
    #检疫费用
    jy = float(0.08) / 100
    jyzd = float(7.1)
    jyfy = max(jy,jyzd)
    file = open('./cache/ck/jyfy.txt','w+')
    file.write(str(jyfy))
    file.close()
    file = open('./cache/ck/jyzsf.txt','w+')
    file.write(str(0))#检疫证书费用，待填写
    file.close()
else:
    file = open('./cache/ck/jyfy.txt','w+')
    file.write(str(0))
    file.close()
    jyfy = 0
    file = open('./cache/ck/jyzsf.txt','w+')
    file.write(str(0))
    file.close()
#报关费
bgf = float(0)
file = open('./cache/ck/bgf.txt','w+')
file.write(str(bgf))
file.close()
#出口货代杂费
ckhdzfl = float(0.25) / 100
ckhdzfmin = float(59.14)
ckhdzf = max(ckhdzfl,ckhdzfmin)
file = open('./cache/ck/ckhdzf.txt','w+')
file.write(str(ckhdzf))
file.close()
#银行费用
yhfy = float(1.77)
file = open('./cache/ck/yhfy.txt','w+')
file.write(str(yhfy))
file.close()
#其他费用

#国内费用合集
gnfyhj = cdzsf + jyfy + bgf + yhfy
file =open('./cache/ck/gnfyhj.txt','w+')
file.write(str(gnfyhj))
file.close()
