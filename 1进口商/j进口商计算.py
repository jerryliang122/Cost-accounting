# -*- coding: utf-8 -*-
import os
import math
import time

mysy = input('贸易术语1FOB/2CRF/3CIF:')
cjj =input('成交价:')
file7 = open('./cache/jk/cjj.txt','a+')
file7.write(cjj)
file7.close()

if mysy == '1':
    cjsl = input('成交数量:')
    baozhuangsldj = input('包装数量(转换到销售数量):')
    djbaozhuangzl=input('包装单件重量:')
    djbaozhuangtj=input('包装单件体积：')
    zl = float(djbaozhuangzl)/float(baozhuangsldj) * float(cjsl)
    tj = float(djbaozhuangtj)/float(baozhuangsldj) * float(cjsl)
    file2 =open('./cache/jk/djbaozhuangzl.txt','a+')
    file2.write(djbaozhuangzl)
    file3 =open('./cache/jk/djbaozhuangtj.txt','a+')
    file3.write(djbaozhuangtj)
    file4 = open('./cache/jk/zl.txt','a+')
    file4.write(str(zl))
    file5 = open('./cache/jk/tj.txt','a+')
    file5.write(str(tj))
    file2.close()
    file3.close()
    file4.close()
    file5.close()
    print('计算运费')
    file6 = open('./cache/jk/mysy.txt','a+')
    file6.write(mysy)
    file6.close()
    time.sleep(2)
    os.system('python3 ./1进口商/运费.py')
    print('计算保险费')
    os.system('python3 ./1进口商/保险费.py')
    print('计算进口税费')
    os.system('python3 ./1进口商/进口税费.py')
    print('计算银行费用')
    os.system('python3 ./1进口商/银行费用.py')
    print('计算其他国内费用')
    os.system('python3 ./1进口商/其他国内费用.py')
    print('计算销货收入')
    os.system('python3 ./1进口商/销货收入.py')
    print('计算预期盈亏率')
    os.system('python3 ./1进口商/预期盈亏额.py')
elif mysy == "2":
    print('计算保险费')
    file6 = open('./cache/jk/mysy.txt','a+')
    file6.write(mysy)
    file6.close()
    os.system('python3 ./1进口商/保险费.py')
    print('计算进口税费')
    os.system('python3 ./1进口商/进口税费.py')
    print('计算银行费用')
    os.system('python3 ./1进口商/银行费用.py')
    print('计算其他国内费用')
    os.system('python3 ./1进口商/其他国内费用.py')
    print('计算销货收入')
    os.system('python3 ./1进口商/销货收入.py')
    print('计算预期盈亏率')
    os.system('python3 ./1进口商/预期盈亏额.py')
elif mysy == '3':
    print('计算进口税费')
    os.system('python3 ./1进口商/进口税费.py')
    print('计算银行费用')
    os.system('python3 ./1进口商/银行费用.py')
    print('计算其他国内费用')
    os.system('python3 ./1进口商/其他国内费用.py')
    print('计算销货收入')
    os.system('python3 ./1进口商/销货收入.py')
    print('计算预期盈亏率')
    os.system('python3 ./1进口商/预期盈亏额.py')