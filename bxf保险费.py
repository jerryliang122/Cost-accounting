# -*- coding: utf-8 -*-
import os
import math
import time

a = raw_input("1进口商/2出口商：")

if a == "1":
    print('尚未支持')
elif a == '2':
    toubaojine = 1.1 
    #读取对外报价文件
    file = open('cache/duiwaibaojia.txt') 
    float(file.read())