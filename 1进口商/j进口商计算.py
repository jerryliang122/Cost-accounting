# -*- coding: utf-8 -*-
import os
import math
import time

mysy = input('贸易术语1FOB/2CRF/3CIF:')
cjj =input('成交价:')

if mysy == '1':
    cjsl = input('成交数量:')
    baozhuangsl = input('包装数量(转换到销售数量):')
    djbaozhuangzl=input('包装单件重量:')
    djbaozhuangtj=input('包装单件体积：')
    zl = float(djbaozhuangzl)/float(baozhuangsl)
    tj = float(djbaozhuangtj)/float(baozhuangsl)
    file1 = open('./cache/jk/baozhuangsl.txt','a')
    print>>file1,baozhuangsl
    file2 =open('./cache/jk/djbaozhuangzl.txt','a')
    print>>file2,baozhuangzl
    file3 =open('./cache/jk/djbaozhuangtj.txt','a')
    print>>file3,djbaozhuangtj
    print('计算运费')
    time.sleep(2)
    os.system('./1进口商/运费.py')
    print('计算保险费')
    os.system('./1进口商/保险费.py')
    print('计算进口税费')
    os.system('./1进口商/进口税费.py')
    print('计算银行费用')
    os.system('./1进口商/银行费用.py')
    print('计算其他国内费用')
    os.system('./1进口商/其他国内费用.py')
    print('计算销货收入')
    os.system('./1进口商/销货收入.py')
    print('计算预期盈亏率')
    os.system('./1进口商/预期盈亏额.py')
if mysy == "2":
    print('计算保险费')
    os.system('./1进口商/保险费.py')
    print('计算进口税费')
    os.system('./1进口商/进口税费.py')
    print('计算银行费用')
    os.system('./1进口商/银行费用.py')
    print('计算其他国内费用')
    os.system('./1进口商/其他国内费用.py')
    print('计算销货收入')
    os.system('./1进口商/销货收入.py')
    print('计算预期盈亏率')
    os.system('./1进口商/预期盈亏额.py')
if mysy == '3':
    print('计算进口税费')
    os.system('./1进口商/进口税费.py')
    print('计算银行费用')
    os.system('./1进口商/银行费用.py')
    print('计算其他国内费用')
    os.system('./1进口商/其他国内费用.py')
    print('计算销货收入')
    os.system('./1进口商/销货收入.py')
    print('计算预期盈亏率')
    os.system('./1进口商/预期盈亏额.py')