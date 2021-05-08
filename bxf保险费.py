# -*- coding: utf-8 -*-
import os
import math
import time

a = float(open('./cache/a.txt').read)
if a == "1":
    print('尚未支持')
elif a == '2':
    toubaojinefl = 1.1
    #读取对外报价文件
    file = open('./cache/duiwaibaojia.txt') 
    toubaojine = float(file.read()) /toubaojinefl
    file1 = open('./cache/baoxianfeilv.txt')
    baoxianfei = float(file1.read()) * toubaojine
    print(baoxianfei)
    print>>open("./cache/baoxianfei.txt",'a'),baoxianfei