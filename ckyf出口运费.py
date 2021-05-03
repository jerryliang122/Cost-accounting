# -*- coding: utf-8 -*-
import os
import math

Transportation = raw_input('使用的交通工具[1空运/2海运]:')
print('在使用浮点计算中计算机因进制转换导致出现误差')
danweitiji =input('单间体积:')
danjianzhongliang = input('单件重量:')
chengjiaoshuliang = input('成交数量:')
#计算公吨和体积
gongdun = danjianzhongliang * chengjiaoshuliang / 1000
gd1 = str(gongdun)
tiji = danweitiji * chengjiaoshuliang
print('公吨' + gd1 )
tj1 = str(tiji)
print('体积' + tj1 )

if Transportation == '1':
    print('暂不支持')
elif Transportation == '2':
    jzx1 = input('20集装箱单价：')
    jzx2 = input('40集装箱单价：')
    jzx3 = input('40h集装箱单价：')
    print('正在计算中')
    #20集装箱的操作方案
    jzx20m = 25
    jzx20c = 33
    m20 = (math.ceil(gongdun / jzx20m))
    c20 = (math.ceil(tiji / jzx20c))
    print(str(max(m20,c20))+ '个20集装箱')
    #40集装箱的操作方案
    jzx40m = 29
    jzx40c = 67
    m40 = (math.ceil(gongdun / jzx40m))
    c40 = (math.ceil(tiji / jzx40c))
    print(str(max(m40,c40))+ '个40集装箱')
    #40H集装箱的操作方案
    jzx40hm = 29
    jzx40hc = 76
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
else:
    print('输入错误。')

file = open('./cache/yunfei.txt','a')
choose = raw_input('1散装/2集装箱：')
if choose == '1':
    print>>file,lcl
elif choose == '2':
    print>>file,jzx