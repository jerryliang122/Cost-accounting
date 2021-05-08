
# -*- coding: utf-8 -*-
import os
import math
import time

print('FOB=1 CFR=2 CIF =3 以此类推')
maoyishuyu = raw_input("使用的是什么贸易术语[FOB/CFR/CIF]:")
shijicaigouchengben = input('实际采购成本:')
baoguanfei = input('报关费：')
qita = input('其他:')
yuqiyingkuilv = input('预期盈亏率:') / 100
baojianshouxufei = input('报检手续费:') / 100
yinhangfeilv = input('银行手续费率：') / 100
baoxianfeilv = input('保险费率，千分率：')/1000
#汇率定义
huilv = input('汇率:')

file1 = open('./cache/yinhangfeilv.txt','a+')
print>>file1,yinhangfeilv
file2 = open('./cache/baojianshouxufei.txt','a+')
print>>file2,baojianshouxufei
file3 = open('./cache/yuqiyingkuilv.txt','a+')
print>>file3,yuqiyingkuilv
file4 = open('./cache/qita.txt','a+')
print>>file4,qita
file5 = open('./cache/baoguanfei.txt','a+')
print>>file5,baoguanfei
file6 = open('./cache/shijicaigouchengben.txt','a+')
print>>file6,shijicaigouchengben
file7 = open("./cache/baoxianfeilv.txt",'a+')
print>>file7,baoxianfeilv
file8 = open('./cache/huilv.txt','a')
print>>file8,huilv
if maoyishuyu == "1":
    fob1 = shijicaigouchengben + baoguanfei + qita
    fob2 = 1 + yuqiyingkuilv
    fob3 = fob1 * fob2
    fob4 = baojianshouxufei + yinhangfeilv
    fob5 = fob2 * fob4
    fob6 = 1 - fob5
    fob7 = fob3 / fob6
    fob = str(fob7*huilv)
    print(fob + 'FOB对外报价')
    file = open('./cache/duiwaibaojia.txt','a+')
    print>>file,fob
elif maoyishuyu == "2":
    print('将在3秒后跳转到出口运费计算')
    time.sleep(3)
    os.system('python ckyf出口运费.py')
    #读取运费脚本的运费
    file = open('./cache/yunfei.txt')  
    chukouyunfei = float(file.read()) / huilv
    
    cfr1 = shijicaigouchengben + baoguanfei + qita + chukouyunfei
    cfr2 = 1 + yuqiyingkuilv
    cfr3 = cfr1 * cfr2
    cfr4 = baojianshouxufei + yinhangfeilv
    cfr5 = cfr2 * cfr4
    cfr6 = 1 - cfr5
    cfr7 = cfr3 / cfr6
    cfr = str(cfr7*huilv)
    print(cfr + 'CFR对外报价')
    file = open('./cache/duiwaibaojia.txt','a')
    print>>file,cfr
elif maoyishuyu == '3':
    #出口运费计算
    print('将在3秒后跳转到出口运费计算')
    time.sleep(3)
    os.system('python ckyf出口运费.py')
    #读取运费脚本的运费
    file = open('./cache/yunfei.txt')  
    chukouyunfei = float(file.read()) / huilv
    #cfr8是保险费率投保加成固定110%
    cif8 = baoxianfeilv * 1.1
    cif1 = shijicaigouchengben + baoguanfei + qita + chukouyunfei
    cif2 = 1 + yuqiyingkuilv
    cif3 = cif1 * cif2
    cif4 = baojianshouxufei + yinhangfeilv + cif8
    cif5 = cif2 * cif4
    cif6 = 1 - cif5
    cif7 = cif3 / cif6
    cif = str(cif7*huilv)
    print(cif + 'CIF对外报价')
    file = open('./cache/duiwaibaojia.txt','a')
    print>>file,cif
else:
    print('输入错误请重新输入。')