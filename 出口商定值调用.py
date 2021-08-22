import os
import math
from sqlitet import setdata 
from sqlitet import readdata
from sqlitet import updatedata
from sqlitet import deldata
import sqlite3
#成交数量
def cjsl():
    yqykv = float(input('预期盈亏率:')) / 100
    setdata('calculated','预期盈亏率',str(yqykv))
    cjsl = input('成交数量:')
    setdata('calculated','成交数量',str(cjsl))
    dj = float(input('单价：')) * readdata('fixed','汇率')
    setdata('calculated','单价',str(dj))
    baozhuangsldj = input('包装数量(转换到销售数量):')
    djbaozhuangzl=input('包装单件重量:')
    djbaozhuangtj=input('包装单件体积：')
    zl = float(djbaozhuangzl)/float(baozhuangsldj) * float(cjsl)
    tj = float(djbaozhuangtj)/float(baozhuangsldj) * float(cjsl)
    bzsl = float(cjsl) / float(baozhuangsldj)
    setdata('calculated','包装数量',str(bzsl))
    setdata('calculated','包装单件重量',str(djbaozhuangzl))
    setdata('calculated','包装单件体积',str(djbaozhuangtj))
    setdata('calculated','包装总重量',str(zl))
    setdata('calculated','包装总体积',str(tj))
    return
    #运费
def yf():
    choose = input('1海运，2航空：')
    setdata('calculated','运输方式',str(choose))
    tj = float(readdata('calculated','体积'))
    zl = float(readdata('calculated','重量'))
    hl = float(readdata('fixed','汇率'))
    if choose == '1':
        jzx1 = float(input('20集装箱单价：')) * hl #有汇率
        jzx2 = float(input('40集装箱单价：')) * hl #有汇率
        jzx3 = float(input('40h集装箱单价：')) * hl #有汇率
        lclhc = float(input('LCL体积单价:')) * hl #有汇率
        lclhm =  float(input('LCL重量单价：')) * hl #有汇率
        setdata('calculated','20集装箱单价',str(jzx1))
        setdata('calculated','40集装箱单价',str(jzx2))
        setdata('calculated','40h集装箱单价',str(jzx3))
        setdata('calculated','LCL体积单价',str(lclhc))
        setdata('calculated','LCL重量单价',str(lclhm))
    else:
        msc = float(input('最低运费msc:'))/float(100) * hl #有汇率
        awc = float(input('AWC操作费：'))
        myc = float(input('MYC燃油费:')) /float(100) * hl #有汇率
        setdata('calculated','MYC燃油费',str(myc))
        setdata('calculated','AWC操作费',str(awc))
        setdata('calculated','最低运费msc',str(msc))
        cbm = tj * float(167)
        hkzl = max(zl,cbm)
        setdata('calculated','航空合同重量',str(hkzl))
        if hkzl < float(45):
            yunjia = input('小于45运价：')
        elif hkzl >= float('45') and hkzl < float('100'):
            yunjia = input('45-100运价:')
        elif hkzl >= float('100') and hkzl < float('300'):
            yunjia = input('100-300运价:')
        elif hkzl >= float('300') and hkzl < float('500'):
            yunjia = input('300-500运价:')
        elif hkzl >= float('500') and hkzl < float('1000'):
            yunjia = input('500-1000运价:')
        else:
            yunjia = input('1000以上运价:')
        setdata('calculated','航空运输价格',str(yunjia))
    return
def cgcb():
    gcjg = float(input('工厂价格:'))
    ts = float(input('退税率:')) / 100
    zzs = float(input('增值税：'))/100 
    setdata('calculated','增值税',str(zzs))
    setdata('calculated','工厂价格',str(gcjg))
    setdata('calculated','退税率',str(ts))
    #检疫费用
    jy = input('有无检疫费用1有/2无：')
    setdata('calculated','有无检疫费用',str(jy))
