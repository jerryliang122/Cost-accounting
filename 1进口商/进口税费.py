# -*- coding: utf-8 -*-
import os
import time
import math
gsl = float(input('输入关税率:')) / 100
xfs = float(input('输入消费税:')) / 100
zzs = float(input('输入增值税:')) / 100
#配置支持CIF
def cif():
    file1 = open('./cache/jk/mysy.txt','a+')
    if file1.read() == '1':
        file2 = open('./cache/jk/yf.txt','a+')
        file3 = open('./cache/jk/htje.txt','a+')
        cfr = float(file2.read()) + float(file3.read())
        file4 = open('./cache/jk/bxf.txt','a+')
        end = cfr + float(file4.read())
        file5 = open('./cache/jk/cif.txt','a+')
        file5.write(str(end))
        file5.close()
    elif file1 == '2':
        file3 = open('./cache/jk/htje.txt','a+')
        file4 = open('./cache/jk/bxf.txt','a+')
        end = float(file3.read()) + float(file4.read())
        file5 = open('./cache/jk/cif.txt','a+')
        file5.write(str(end))
        file5.close()
    else:
        pass
    return end