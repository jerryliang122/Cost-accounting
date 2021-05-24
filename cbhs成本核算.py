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
    if mysy == '1':
        pass
    elif mysy == '2':
        出口商定值调用.yf()
    else:
        pass
    
    os.system('python3 ./2出口商/出口商计算.py')

        
else:
    print('输入错误')
    os.system('python3 cbhs成本核算.py')