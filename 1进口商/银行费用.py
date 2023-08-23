# -*- coding: utf-8 -*-
import os
import time
import math

yhxz = input('1汇款/2托收/3信用证：')

def hk():
    ff = input('1电汇/2票汇:')
    dfzg = 29.57 if ff == '1' else 35.49
    dhfl = float(1) / 1000 * float(open('./cache/jk/cif.txt').read())
    dh = min(dhfl,dfzg)
    print(dh)
    with open('./cache/jk/yhfy.txt','a+') as file:
        file.write(str(dh))
    return dh

def ts():
    file = open('./cache/jk/cjj.txt')
    #托收费用不一定固定目前按固定算
    ts = float(file) * 0.1 / 100
    with open('./cache/jk/yhfy.txt','a+') as file:
        file.write(str(ts))
    return ts

def xyz():
    file = open('./cache/jk/cjj.txt')
    xyzfl = float(file) * 0.15 / 100
    xyzzg = 23.66
    xyz = max(xyzfl,xyzzg)
    with open('./cache/jk/yhfy.txt','a+') as file:
        file.write(str(xyz))
    return xyz

qt = float(0) #其他费用

if yhxz == '1':
    hj = hk() + qt
    print(hj)
    file = open('./cache/jk/yhfyhj.txt','a+')
    file.write(str(hj))
elif yhxz == '2':
    hj = ts() + qt
    print(hj)
    file = open('./cache/jk/yhfyhj.txt','a+')
    file.write(str(hj))
else:
    hj = xyz() + qt
    print(hj)
    file = open('./cache/jk/yhfyhj.txt','a+')
    ffile.write(str(hj))
file.close()