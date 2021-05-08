# -*- coding: utf-8 -*-
import os
import math
import time

file = open('./cache/a.txt')
a = float(file.read())
#进口商
if a == '1':
    pass
#出口商
elif a == "2":
    jianyifelv = float(open('./cache/baojianshouxufei.txt').read)
    hetongjinge = float(open('./cache/duiwaibaojia.txt').read)
    jianyifeiyong = hetongjinge * jianyifelv
    print>>open('./cache/jianyifeiyong.txt','a'),jianyifeiyong