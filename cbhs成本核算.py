import os
import time

print('欢迎使用新版成本核算')
print('正在初始化文件夹')
os.system('rm -rf ./cache/*')
os.system('mkdir ./cache/jk')
os.system('mkdir ./cache/ck')
choose = input('1进口商/2出口商:')
if  choose == "1":
    print('正在启动进口商计算')
    os.system('./1进口商/j进口商计算.py')
elif choose == "2":
    print('正在启动出口商计算')
    os.system('./2出口商/出口商计算.py')