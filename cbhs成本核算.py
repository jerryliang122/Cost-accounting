# -*- coding: utf-8 -*-
import os
import math
import time

print('欢迎使用python版本的成本核算--作者jerryliang')
time.sleep(3)
print('版本0.1alpha----注意请使用小写英文--费率是写入%')
time.sleep(2)
print('正在初始化cache文件夹中')
os.system('rm -rf ./cache/')
time.sleep(2)
#对外报价
a = raw_input('1进口商/2出口商:')
if a =="2":
    print('对外报价计算，正在跳转至相关模块')
    time.sleep(1)
    os.system('python dwbj对外报价.py')
if a =='1':
    print('进口报价计算，正在跳转至相关模块')
    time.sleep(1)
    