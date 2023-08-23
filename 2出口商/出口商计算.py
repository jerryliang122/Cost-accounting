# -*- coding: utf-8 -*-
import os
import math
import time

mysy = open('./cache/ck/mysy.txt').read()
if mysy == '1':
    os.system('python3 ./2出口商/采购成本.py')
    os.system('python3 ./2出口商/对外报价.py')
elif mysy == '2':
    os.system('python3 ./2出口商/采购成本.py')
    os.system('python3 ./2出口商/对外报价.py')
    os.system('python3 ./2出口商/运费.py')
else:
    os.system('python3 ./2出口商/采购成本.py')
    os.system('python3 ./2出口商/对外报价.py')
    os.system('python3 ./2出口商/运费.py')
    os.system('python3 ./2出口商/保险费.py')
os.system('python3 ./2出口商/国内费用.py')
os.system('python3 ./2出口商/预期盈亏率.py')
ykv = float(open('./cache/ck/ykv.txt').read()) / 100
yqykv = float(open('./cache/ck/yqykv.txt').read())
print('.......................................')
print('对外报价:'+ open('./cache/ck/dwbj.txt').read())
print('单价'+ open('./cache/ck/dj.txt').read())
print('美元单价:'+str(float(open('./cache/ck/dj.txt').read())/0.875))
print('购货价格:'+ open('./cache/ck/ghjg.txt').read())
print('退税收入:'+open('./cache/ck/tssl.txt').read())
print('采购成本合计:'+open('./cache/ck/cgcbhj.txt').read())
print('国内费用.......')
print('产地证书费:'+open('./cache/ck/cdzsf.txt').read())
print('出口检验检疫费:'+open('./cache/ck/jyfy.txt').read())
print('检疫证书费:'+ open('./cache/ck/jyzsf.txt').read())
print('出口报关费:'+ open('./cache/ck/bgf.txt').read())
print('出口货代杂费'+ open('./cache/ck/ckhdzf.txt').read())
print('银行费用:'+ open('./cache/ck/yhfy.txt').read())
print('其他费用：0')
print('国内费用合计:'+open('./cache/ck/gnfyhj.txt').read())
if mysy == '1':
    pass
elif mysy == '2':
    print('包装数量:'+ open('./cache/ck/bzsl.txt').read())
    print('总毛重'+ open('./cache/ck/zl.txt').read())
    print('总体积'+ open('./cache/ck/tj.txt').read())
    print('运费:'+ open('./cache/ck/yf.txt').read()+open('./cache/ck/hy-ysfs.txt').read())
else:
    print('包装数量:'+ open('./cache/ck/bzsl.txt').read())
    print('总毛重'+ open('./cache/ck/zl.txt').read())
    print('总体积'+ open('./cache/ck/tj.txt').read())
    print('运费:'+ open('./cache/ck/yf.txt').read()+open('./cache/ck/hy-ysfs.txt').read())
    print('投保金额'+ open('./cache/ck/bxje.txt').read())
    print('保险费'+ open('./cache/ck/bxf.txt').read())
print("预期盈亏率"+open('./cache/ck/ykv.txt').read())
print('预期盈亏额'+ open('./cache/ck/yke.txt').read())
