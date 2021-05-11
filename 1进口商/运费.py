# -*- coding: utf-8 -*-
import os
import math
import time

yf =input('1海运/2空运:')
#打开存储文件
zl = float(open('./cache/jk/zl.txt','r+').read()) / 1000
tj = float(open('./cache/jk/tj.txt','r+').read()) 

if yf == "1":
    jzx1 = input('20集装箱单价：')
    jzx2 = input('40集装箱单价：')
    jzx3 = input('40h集装箱单价：')
    print('正在计算中')
    #20集装箱的操作方案
    jzx20m = float(25)
    jzx20c = float(33)
    m20 = zl/jzx20m
    c20 = tj/jzx20c
    print(str(max(m20,c20))+ '个20集装箱')
    #40集装箱的操作方案
    jzx40m = float(29)
    jzx40c = float(67)
    m40 = zl/jzx40m
    c40 = tj/jzx40m
    print(str(max(m40,c40))+ '个40集装箱')
    #40H集装箱的操作方案
    jzx40hm = float(29)
    jzx40hc = float(76)
    m40h = (math.ceil(gongdun / jzx40hm))
    c40h = (math.ceil(tiji /jzx40hc))
    print(str(max(m40h,c40h))+ '个40h集装箱')
    #20集装箱输出价格
    jzx20 = (max(m20,c20))
    jzx20a = jzx20 * jzx1
    print('\n20集装箱价格'+str(jzx20a))
    #40集装箱输出价格
    jzx40 = (max(m40,c40))
    jzx40a = jzx40 * jzx2
    print('\n40集装箱价格'+str(jzx40a))
    #40H集装箱输出价格
    jzx40h = (max(m40h,c40h))
    jzx40ha = jzx40h * jzx3
    print('\n40h集装箱价格'+str(jzx40ha))
    print('下面散装价格\n')
    #LCLM 公吨输出价格
    lclhm = input('LCL重量单价：')
    lclhm1 = lclhm * gongdun
    lclhc = input('LCL体积单价:')
    lclhc1 = lclhm * tiji
    print(str(lclhc1)+ ' 体积价格')
    print(str(lclhm1)+ '重量价格')
    lcl = max(lclhc1,lclhm1)
    print(str(lcl) + '散件价格' )
    #
    jzx = min(jzx40ha,jzx20a,jzx40a)
    print(str(jzx) + '集装箱价格' )    
    
elif yf == '2':
    pass
else:
    print('输入错误')
    os.system('python3 ./1进口商/运费.py')

