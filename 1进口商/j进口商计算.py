# -*- coding: utf-8 -*-
import os
import math
import time

mysy = input('贸易术语1FOB/2CRF/3CIF:')
cjj =float(input('成交价:')) * 0.879
file7 = open('./cache/jk/cjj.txt','a+')
file7.write(str(cjj))
file7.close()
file6 = open('./cache/jk/mysy.txt','a+')
file6.write(mysy)
file6.close()
yf =input('1海运/2空运:')
#打开存储文件
ysfs = open('./cache/jk/ysfs.txt',"a+")
ysfs.write(yf)
ysfs.close()
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
    print('计算完毕 ')
    time.sleep(1)
    #包装数量
    bzsl = float(cjsl) / float(baozhuangsldj)
    print('包装数量'+ str(bzsl))
    print('重量:'+ open('./cache/jk/zl.txt').read())
    print('体积:'+ open('./cache/jk/tj.txt').read())
    print('运费:'+ open('./cache/jk/yf.txt').read()+open('./cache/jk/ysfs.txt').read())
    print('保险金额:'+ open('./cache/jk/bxje.txt').read())
    print('保险费:'+ open('./cache/jk/bxf.txt').read())
elif mysy == "2":
    file = open('./cache/jk/yf.txt','a+')
    file.write('0')
    file.close()
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
    print('保险金额:'+ open('./cache/jk/bxje.txt').read())
    print('保险费:'+ open('./cache/jk/bxf.txt').read())
elif mysy == '3':
    file = open('./cache/jk/yf.txt','a+')
    file.write('0')
    file.close()
    file = open('./cache/jk/bxf.txt','a+')
    file.write('0')
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

print('成交价:'+ open('./cache/jk/cjj.txt').read())
print('进口税费：')
print('进口关税:'+ open('./cache/jk/jkgs.txt').read())
print('进口增值税：'+ open('./cache/jk/jkzzs.txt').read())
print('进口消费税'+ open('./cache/jk/jkxfs.txt').read())
print('进口税费合计:'+ open('./cache/jk/jksfhj.txt').read())
print('银行费用：')
print('银行收款费用:'+ open('./cache/jk/yhfy.txt').read())
print('银行合计费用:'+ open('./cache/jk/yhfyhj.txt').read())
print('其他国内费用:')
print('进口检验检疫费：'+ open('./cache/jk/jyfy.txt').read())
print('进口报关费:'+ open('./cache/jk/bgf.txt').read())
print('进口货代杂费:'+ open('./cache/jk/hdzf.txt').read())
print('其他国内费用合计：'+ open('./cache/jk/gnfyhy.txt').read())
print(' 销货收入:'+ open('./cache/jk/xhsl.txt').read())
print('预期盈亏额: ')
print('预期盈亏额:'+ open('./cache/jk/yqyke.txt').read())
print('盈亏率:'+ open('./cache/jk/ykl.txt').read())
