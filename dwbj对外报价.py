
# -*- coding: utf-8 -*-
import os
import math
import time

maoyishuyu = raw_input("使用的是什么贸易术语[FOB/CFR/CIF]:")
shijicaigouchengben = input('实际采购成本:')
baoguanfei = input('报关费：')
qita = input('其他:')
yuqiyingkuilv = input('预期盈亏率:') / 100
baojianshouxufei = input('报检手续费:') / 100
yinhangfeilv = input('银行手续费率：') / 100
#汇率定义
huilv = 1.14

if maoyishuyu == "fob":
    fob1 = shijicaigouchengben + baoguanfei + qita
    fob2 = 1 + yuqiyingkuilv
    fob3 = fob1 * fob2
    fob4 = baojianshouxufei + yinhangfeilv
    fob5 = fob2 * fob4
    fob6 = 1 - fob5
    fob7 = fob3 / fob6
    print(str(fob7*huilv)+ 'FOB对外报价')
elif maoyishuyu == "cfr":
    print('将在3秒后跳转到出口运费计算')
    time.sleep(3)
    os.system('python ckyf出口运费.py')
    chukouyunfei = input('出口运费（美元）:') / huilv
    
    cfr1 = shijicaigouchengben + baoguanfei + qita + chukouyunfei
    cfr2 = 1 + yuqiyingkuilv
    cfr3 = cfr1 * cfr2
    cfr4 = baojianshouxufei + yinhangfeilv
    cfr5 = cfr2 * cfr4
    cfr6 = 1 - cfr5
    cfr7 = cfr3 / cfr6
    print(str(cfr7*huilv)+ 'CFR对外报价')
elif maoyishuyu == 'cif':
    #出口运费计算
    print('将在3秒后跳转到出口运费计算')
    time.sleep(3)
    os.system('python ckyf出口运费.py')
    chukouyunfei = input('出口运费（美元）:') / huilv
    #cfr8是保险费率投保加成固定110%
    baoxianfeilv = input('保险费率：')
    cif8 = baoxianfeilv * 1.1
    cif1 = shijicaigouchengben + baoguanfei + qita + chukouyunfei
    cif2 = 1 + yuqiyingkuilv
    cif3 = cif1 * cif2
    cif4 = baojianshouxufei + yinhangfeilv + cif8
    cif5 = cif2 * cif4
    cif6 = 1 - cif5
    cif7 = cif3 / cif6
    print(str(cif7*huilv)+ 'CIF对外报价')
else:
    print('输入错误请重新输入。')