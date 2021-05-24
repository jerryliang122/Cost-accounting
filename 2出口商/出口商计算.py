# -*- coding: utf-8 -*-
import os
import math
import time

mysy = open('./cache/ck/mysy.txt').read()
if mysy == '1':
    os.system('python3 ./2出口商/采购成本.py')
    os.system('python3 ./2出口商/对外报价.py')
    os.system('python3./2出口商/国内费用.py')
    os.system('python3 ./2出口商/预期盈亏率.py')
    pass
elif mysy == '2':
    os.system('python3 ./2出口商/采购成本.py')
    os.system('python3 ./2出口商/对外报价.py')
    os.system('python3 ./2出口商/运费.py')
    os.system('python3./2出口商/国内费用.py')
    os.system('python3 ./2出口商/预期盈亏率.py')
    pass
else:
    os.system('python3 ./2出口商/采购成本.py')
    os.system('python3 ./2出口商/对外报价.py')
    os.system('python3 ./2出口商/运费.py')
    os.system('python3 ./2出口商/保险费.py')
    os.system('python3./2出口商/国内费用.py')
    os.system('python3 ./2出口商/预期盈亏率.py')
    pass
