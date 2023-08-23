# -*- coding: utf-8 -*-
import os
import time
import math
gsl = float(input('输入关税率:')) / 100
xfs = float(input('输入消费税:')) / 100
zzs = float(input('输入增值税:')) / 100
#配置支持CIF
def cif():
    file1 = open('./cache/jk/mysy.txt').read()
    if file1 == '1':
        file2 = open('./cache/jk/yf.txt')
        file3 = open('./cache/jk/cjj.txt')
        cfr = float(file2.read()) + float(file3.read())
        file4 = open('./cache/jk/bxf.txt')
        end = cfr + float(file4.read())
        with open('./cache/jk/cif.txt','a+') as file5:
            file5.write(str(end))
    elif file1 == '2':
        file3 = open('./cache/jk/cjj.txt')
        file4 = open('./cache/jk/bxf.txt')
        end = float(file3.read()) + float(file4.read())
        with open('./cache/jk/cif.txt','a+') as file5:
            file5.write(str(end))
        yfhj = open('./cache/jk/yf.txt','w+')
        yfhj.close()
    else:
        file6 = open('./cache/jk/cjj.txt').read()
        end = float(file6)
        with open('./cache/jk/yf.txt','w+') as yfhj:
            bxfhj = open('./cache/jk/bxf.txt','w+')
            yfhj.write('0')
            bxfhj.write('0')
        bxfhj.close()
    return end
ciff = cif()
jkgs = ciff * gsl
wscb = ciff + jkgs
jkxfs = wscb * xfs / (1-xfs)
jkzzs = (wscb+jkxfs) * zzs
jksfhj = jkgs + jkxfs + jkzzs
with open('./cache/jk/jkgs.txt',"a+") as file1:
    file2 = open('./cache/jk/wscb.txt','a+')
    file3 = open('./cache/jk/jkxfs.txt','a+')
    file4 = open('./cache/jk/jkzzs.txt','a+')
    file5 = open('./cache/jk/jksfhj.txt','a+')
    file1.write(str(jkgs))
    file2.write(str(wscb))
    file3.write(str(jkxfs))
    file4.write(str(jkzzs))
    file5.write(str(jksfhj))
file2.close()
file3.close()
file4.close()
file5.close()