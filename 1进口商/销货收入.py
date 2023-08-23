# -*- coding: utf-8 -*-
import os
import time
import math

cjsl = float(input('成交数量:'))
gnsl = float(input('国内售价：'))

xhsr = cjsl * gnsl
with open('./cache/jk/xhsl.txt',"a+") as file:
    file.write(str(xhsr))