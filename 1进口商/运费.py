# -*- coding: utf-8 -*-
import os
import math
import time

yf =input('1海运/2空运:')
#打开存储文件
ysfs = open('./cache/jk/ysfs.txt',"a+")
ysfs.write(yf)
ysfs.close()
#海运计费
if yf == "1":
    zl = float(open('./cache/jk/zl.txt').read()) / 1000
    tj = float(open('./cache/jk/tj.txt').read())
    jzx1 = float(input('20集装箱单价：')) * 0.875
    jzx2 = float(input('40集装箱单价：')) * 0.875
    jzx3 = float(input('40h集装箱单价：')) * 0.875
    print('正在计算中')
    #20集装箱的操作方案
    jzx20m = float(25)
    jzx20c = float(33)
    m20 = zl/jzx20m
    c20 = tj/jzx20c
    print(str(math.ceil(max(m20,c20)))+ '个20集装箱')
    #40集装箱的操作方案
    jzx40m = float(29)
    jzx40c = float(67)
    m40 = zl/jzx40m
    c40 = tj/jzx40m
    print(str(math.ceil(max(m40,c40)))+ '个40集装箱')
    #40H集装箱
    # 的操作方案
    jzx40hm = float(29)
    jzx40hc = float(76)
    m40h = zl/jzx40hm
    c40h = tj/jzx40hc
    print(str(math.ceil(max(m40h,c40h)))+ '个40h集装箱')
    #20集装箱输出价格
    jzx20 = math.ceil(max(m20,c20))
    jzx20a = jzx20 * jzx1
    print('\n20集装箱价格'+str(jzx20a))
    #40集装箱输出价格
    jzx40 = math.ceil(max(m40,c40))
    jzx40a = jzx40 * jzx2
    print('\n40集装箱价格'+str(jzx40a))
    #40H集装箱输出价格
    jzx40h = math.ceil(max(m40h,c40h))
    jzx40ha = jzx40h * jzx3
    print('\n40h集装箱价格'+str(jzx40ha))
    print('下面散装价格\n')
    #LCLM 公吨输出价格
    lclhm =  float(input('LCL重量单价：')) * 0.875
    lclhm1 = lclhm * zl
    lclhc = float(input('LCL体积单价:')) * 0.875
    lclhc1 = lclhc * tj
    print(str(lclhc1)+ ' 体积价格')
    print(str(lclhm1)+ '重量价格')
    lcl = max(lclhc1,lclhm1)
    print(str(lcl) + '散件价格' )
    jzx = min(jzx40ha,jzx20a,jzx40a)
    print(str(jzx) + '集装箱价格' )    
    if lcl > jzx :
        print(str(jzx) + '集装箱价格' )
        file1 = open('./cache/jk/yf.txt','a+')
        file1.write(str(jzx))
    else:
        print(str(lcl) + '散件价格')     
        file1 = open('./cache/jk/yf.txt','a+')
        file1.write(str(lcl))
#航空计费
elif yf == '2':
    zl = float(open('./cache/jk/zl.txt').read()) 
    tj = float(open('./cache/jk/tj.txt').read())
    cbm = tj * float('167')
    hkzl = max(zl,cbm)
    msc = float(input('最低运费msc:'))/float(100) * 0.875
    awc = float(input('AWC操作费：'))
    myc = float(input('MYC燃油费:')) /float(100) * 0.875
    if hkzl < float('45'):
        yunjia = input('小于45运价:')
        #计算运费
        end = hkzl * float(yunjia)
        fjf = awc + hkzl * myc + msc * hkzl
        hkyf = round((end + fjf)*0.875,2)
        file3 = open('./cache/jk/hkyf.txt','a+')
        file3.write(str(hkyf))
        file3.close()
    elif hkzl >= float('45') and hkzl < float('100'):
        yunjia = input('45-100运价:')
        #计算运费
        end = hkzl * float(yunjia)
        fjf = awc + hkzl * myc + msc * hkzl
        hkyf = round((end + fjf)*0.875,2)
        file3 = open('./cache/jk/hkyf.txt','a+')
        file3.write(str(hkyf))
        file3.close()
    elif hkzl >= float('100') and hkzl < float('300'):
        yunjia = input('100-300运价:')
        #计算运费
        end = hkzl * float(yunjia)
        fjf = awc + hkzl * myc + msc * hkzl
        hkyf = round((end + fjf)*0.875,2)
        file3 = open('./cache/jk/hkyf.txt','a+')
        file3.write(str(hkyf))
        file3.close()
    elif hkzl >= float('300') and hkzl < float('500'):
        yunjia = input('300-500运价:')
        #计算运费
        end = hkzl * float(yunjia)
        fjf = awc + hkzl * myc + msc * hkzl
        hkyf = round((end + fjf)*0.875,2)
        file3 = open('./cache/jk/hkyf.txt','a+')
        file3.write(str(hkyf))
        file3.close()
    elif hkzl >= float('500') and hkzl < float('1000'):
        yunjia = input('500-1000运价:')
        #计算运费
        end = hkzl * float(yunjia)
        fjf = awc + hkzl * myc + msc * hkzl
        hkyf = round((end + fjf)*0.875,2)
        file3 = open('./cache/jk/hkyf.txt','a+')
        file3.write(str(hkyf))
        file3.close()
    else:
        yunjia = input('1000以上运价:')
        #计算运费
        end = hkzl * float(yunjia)
        fjf = awc + hkzl * myc + msc * hkzl
        hkyf = round((end + fjf)*0.875,2)
        file3 = open('./cache/jk/hkyf.txt','a+')
        file3.write(str(hkyf))
        file3.close()
else:
    print('输入错误')
    os.system('python3 ./1进口商/运费.py')

