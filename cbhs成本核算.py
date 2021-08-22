# -*- coding: utf-8 -*-
import os
import time
import 出口商定值调用
import os
import sqlite3
from sqlitet import setdata 
from sqlitet import readdata
from sqlitet import updatedata
from sqlitet import deldata
print('欢迎使用新版成本核算')
print('正在初始化数据库')
#sqlit检查目录下是否有文件
sql = os.path.exists('sql.db')
if not sql:
    conn = sqlite3.connect('sql.db')
    c = conn.cursor()
    c.execute('CREATE TABLE fixed ( name TEXT NULL , value TEXT NULL );')
    c.execute('CREATE TABLE calculated ( name TEXT NULL , Value TEXT NULL );')
    conn.commit()
    hl = float(input('汇率:')) 
    setdata('fixed','汇率',str(hl))
    conn.commit()
else:
    database = input('您不是第一次使用本程序，是否初始化[y/n]:')
    if database =='y':
        os.remove('sql.db')
        conn = sqlite3.connect('sql.db')
        c = conn.cursor()
        c.execute('CREATE TABLE fixed ( name TEXT NULL , value TEXT NULL );')
        c.execute('CREATE TABLE calculated ( name TEXT NULL , Value TEXT NULL );')
        hl = float(input('汇率:')) 
        setdata('fixed','汇率',str(hl))
        conn.commit()
    else:
        conn = sqlite3.connect('sql.db')
        c = conn.cursor()
        c.execute('drop table calculated')
conn.close()
choose = input('1进口商/2出口商:')
if  choose == "1":
    print('正在启动进口商计算')
    os.system('python3 ./1进口商/j进口商计算.py')
elif choose == "2":
    print('正在启动出口商计算')
    mysy = input('贸易术语1FOB/2CRF/3CIF:')
    setdata("fixed",'贸易术语',str(mysy))
    出口商定值调用.cjsl()
    出口商定值调用.cgcb()
    if mysy == '1':
        pass
    elif mysy == '2':
        出口商定值调用.yf()
    else:
        出口商定值调用.yf()
        pass
    os.system('python3 ./2出口商/出口商计算.py')
    while True:
        dj = open('./cache/ck/dj.txt').read()
        djj = float(dj) + 0.01
        flie = open('./cache/ck/dj.txt','w+')
        flie.write(str(djj))
        flie.close()
        ykv = float(open('./cache/ck/ykv.txt').read()) / 100
        yqykv = float(open('./cache/ck/yqykv.txt').read()) 
        if ykv < yqykv :
            os.system('python3 ./2出口商/出口商计算.py')
        else:
            break

        
else:
    print('输入错误')
    os.system('python3 cbhs成本核算.py')