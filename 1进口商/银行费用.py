# -*- coding: utf-8 -*-
import os
import time
import math

yhxz = input('1汇款/2托收/3信用证/4其他：')

def hk():
    ff = input('1电汇/2票汇:')
    if ff == '1':
        dhfl = float(input('票汇手续费：')) / 100 * float(open('./cache/jk/cif.txt'))
        dfzg = float(input('票汇最高手续费:'))
        dh = min(dhfl,dfzg)
        print(str(dh))
        file = open('./cache/jk/yhfy.txt','a+')
        file.write(str(dh))
        file.close()
    else:
        dhfl = float(input('票汇手续费：')) / 100 * float(open('./cache/jk/cif.txt'))
        dfzg = float(input('票汇最高手续费:'))
        dh = min(dhfl,dfzg)
        print(str(dh))
        file = open('./cache/jk/yhfy.txt','a+')
        file.write(str(dh))
        file.close()
    return dh
def ts():
    file = open('./cache/jk/cjj.txt','a+')
    #托收费用不一定固定目前按固定算
    ts = float(file) * 0.1 / 100