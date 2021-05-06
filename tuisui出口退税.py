# -*- coding: utf-8 -*-
import os
import math
import time

zengzhishui = input('增值税:') / 100
tuishuilv =input('退税率：') / 100
print>>open('./cache/zengzhishui.txt','a'),zengzhishui
print>>open('./cache/tuishuilv.txt','a'),tuishuilv
a = 1+ zengzhishui
tuishuie = float(open('./cache/shijicaigouchengben.txt').read())/a*tuishuilv
print>>open('./cache/tuishui.txt',"a")