# -*- coding: utf-8 -*-
import os
import math
import time


#打开存储文件
ysfs = open('./cache/ck/ysfs.txt').read()
yf = ysfs
#海运计费
if yf == "1":
    zl = float(open('./cache/ck/zl.txt').read()) / 1000
    tj = float(open('./cache/ck/tj.txt').read())
    #print('正在计算中')
    #20集装箱的操作方案
    jzx20m = float(25)
    jzx20c = float(33)
    m20 = zl/jzx20m
    c20 = tj/jzx20c
    #print(str(math.ceil(max(m20,c20)))+ '个20集装箱')
    #40集装箱的操作方案
    jzx40m = float(29)
    jzx40c = float(67)
    m40 = zl/jzx40m
    c40 = tj/jzx40m
    #print(str(math.ceil(max(m40,c40)))+ '个40集装箱')
    #40H集装箱
    # 的操作方案
    jzx40hm = float(29)
    jzx40hc = float(76)
    m40h = zl/jzx40hm
    c40h = tj/jzx40hc
    #print(str(math.ceil(max(m40h,c40h)))+ '个40h集装箱')
    #20集装箱输出价格
    jzx1 = float(open('./cache/ck/jzx1.txt').read())
    jzx2 = float(open('./cache/ck/jzx2.txt').read())
    jzx3 = float(open('./cache/ck/jzx3.txt').read())
    lclhc = float(open('./cache/ck/lclhc.txt').read())
    lclhm = float(open('./cache/ck/lclhm.txt').read())
    jzx20 = math.ceil(max(m20,c20))
    jzx20a = jzx20 * jzx1 * 0.875 #有汇率
    #print('\n20集装箱价格'+str(jzx20a))
    #40集装箱输出价格
    jzx40 = math.ceil(max(m40,c40))
    jzx40a = jzx40 * jzx2 * 0.875 #有汇率
    #print('\n40集装箱价格'+str(jzx40a))
    #40H集装箱输出价格
    jzx40h = math.ceil(max(m40h,c40h))
    jzx40ha = jzx40h * jzx3 * 0.875 #有汇率
    #print('\n40h集装箱价格'+str(jzx40ha))
    #print('下面散装价格\n')
    #LCLM 公吨输出价格

    lclhm1 = lclhm * zl * 0.875 #有汇率

    lclhc1 = lclhc * tj * 0.875 #有汇率
    #print(str(lclhc1)+ ' 体积价格')
    #print(str(lclhm1)+ '重量价格')
    lcl = max(lclhc1,lclhm1)
    #print(str(lcl) + '散件价格' )
    jzx = min(jzx40ha,jzx20a,jzx40a)
    #print(str(jzx) + '集装箱价格' )
    if lcl > jzx:
        with open('./cache/ck/yf.txt','w+') as file1:
            file1.write(str(jzx))
        file = open('./cache/ck/hy-ysfs.txt','w+')
        file.write('集装箱')
    else:
        #print(str(lcl) + '散件价格')     
        file1 = open('./cache/ck/yf.txt','w+')
        file1.write(str(lcl))
        file = open('./cache/ck/hy-ysfs.txt','w+')
        file.write('散货')
    file.close()
elif yf == '2':
    with open('./cache/ck/hy-ysfs.txt','w+') as file:
        file.write('')
    yunjia = float(open('./cache/ck/yunjia.txt').read())
    hkzl = float(open('./cache/ck/htzl.txt').read())
    awc = float(open('./cache/ck/awc.txt').read())
    msc = float(open('./cache/ck/msc.txt').read())
    myc = float(open('./cache/ck/myc.txt').read())
        #计算运费
    end = hkzl * yunjia
    fjf = awc + hkzl * myc + msc * hkzl
    #有汇率
    yf = round((end + fjf)*0.875,2)
    with open('./cache/ck/yf.txt','w+') as file3:
        file3.write(str(yf))
else:
    #print('输入错误')
    os.system('python3 ./出口商/运费.py')

