# -*- coding: utf-8 -*-
import os
import math
import time 
file = open('./cache/ck/mysy.txt').read()
yqykl = float(input('预期盈亏率:')) / 100
cgcb = float(open('./cache/ck/cgcbhj.txt').read())
bgf = float(11.83)
file = open('./cache/ck/bgf.txt','a+')
file.write(str(bgf))
file.close()
if  file == '1':
    pass