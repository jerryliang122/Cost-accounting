# -*- coding: utf-8 -*-
import os
import time
import 出口商定值调用

print('欢迎使用新版成本核算')
print('正在初始化文件夹')
os.system('rm -rf ./cache/*')
os.system('mkdir ./cache')
os.system('mkdir ./cache/jk')
os.system('mkdir ./cache/ck')
choose = input('1进口商/2出口商:')
if  choose == "1":
    print('正在启动进口商计算')
    os.system('python3 ./1进口商/j进口商计算.py')
elif choose == "2":
    print('正在启动出口商计算')
    mysy = input('贸易术语1FOB/2CRF/3CIF:')
    file6 = open('./cache/ck/mysy.txt','a+')
    file6.write(mysy)
    file6.close()
    出口商定值调用.cjsl()
    出口商定值调用.cgcb()
    if mysy == '1':
        pass
    elif mysy == '2':
        出口商定值调用.yf()
    else:
        出口商定值调用.yf()
        pass
    os.system('python3 ./2出口商/出口商计算.py')
    while True:
        dj = open('./cache/ck/dj.txt').read()
        djj = float(dj) + 0.01
        flie = open('./cache/ck/dj.txt','w+')
        flie.write(str(djj))
        flie.close()
        ykv = float(open('./cache/ck/ykv.txt').read()) / 100
        yqykv = float(open('./cache/ck/yqykv.txt').read()) 
        if ykv < yqykv :
            os.system('python3 ./2出口商/出口商计算.py')
        else:
            break

        
else:
    print('输入错误')
    os.system('python3 cbhs成本核算.py')