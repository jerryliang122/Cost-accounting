# -*- coding: utf-8 -*-
import os
import time
import math

yhxz = input('1汇款/2托收/3信用证：')

def hk():
    ff = input('1电汇/2票汇:')
    if ff == '1':
        dhfl = float(1) / 1000 * float(open('./cache/jk/cif.txt').read())
        dfzg = 29.57 #电汇最高金额
        dh = min(dhfl,dfzg)
        print(str(dh))
        file = open('./cache/jk/yhfy.txt','a+')
        file.write(str(dh))
        file.close()
    else:
        dhfl = float(1) / 1000 * float(open('./cache/jk/cif.txt').read())
        dfzg = 35.49 #票汇最高金额
        dh = min(dhfl,dfzg)
        print(str(dh))
        file = open('./cache/jk/yhfy.txt','a+')
        file.write(str(dh))
        file.close()
    return dh

def ts():
    file = open('./cache/jk/cjj.txt')
    #托收费用不一定固定目前按固定算
    ts = float(file) * 0.1 / 100
    file = open('./cache/jk/yhfy.txt','a+')
    file.write(str(ts))
    file.close()
    return ts

def xyz():
    file = open('./cache/jk/cjj.txt')
    xyzfl = float(file) * 0.15 / 100 
    xyzzg = float(23.66) #开证手续费
    xyz = max(xyzfl,xyzzg)
    file = open('./cache/jk/yhfy.txt','a+')
    file.write(str(xyz))
    file.close()
    return xyz

qt = float(0) #其他费用

if yhxz == '1':
    hj = hk() + qt
    print(str(hj))
    file = open('./cache/jk/yhfyhj.txt','a+')
    file.write(str(hj))
    file.close()
elif yhxz == '2':
    hj = ts() + qt
    print(str(hj))
    file = open('./cache/jk/yhfyhj.txt','a+')
    file.write(str(hj))
    file.close()
else:
    hj = xyz() + qt
    print(str(hj))
    file = open('./cache/jk/yhfyhj.txt','a+')
    ffile.write(str(hj))
    file.close()