import os
import math
#成交数量
def cjsl():
    yqykv = float(input('预期盈亏率:')) / 100
    with open('./cache/ck/yqykv.txt','a+') as file:
        file.write(str(yqykv))
    cjsl = input('成交数量:')
    with open('./cache/ck/cjsl.txt','a+') as file:
        file.write(cjsl)
    dj = float(input('单价：')) * 0.875 #有汇率
    with open('./cache/ck/dj.txt','a+') as file:
        file.write(str(dj))
    baozhuangsldj = input('包装数量(转换到销售数量):')
    djbaozhuangzl=input('包装单件重量:')
    djbaozhuangtj=input('包装单件体积：')
    zl = float(djbaozhuangzl)/float(baozhuangsldj) * float(cjsl)
    tj = float(djbaozhuangtj)/float(baozhuangsldj) * float(cjsl)
    bzsl = float(cjsl) / float(baozhuangsldj)
    with open('./cache/ck/bzsl.txt','a+') as file:
        file.write(str(bzsl))
    with open('./cache/ck/djbaozhuangzl.txt','a+') as file2:
        file2.write(djbaozhuangzl)
        file3 =open('./cache/ck/djbaozhuangtj.txt','a+')
        file3.write(djbaozhuangtj)
        file4 = open('./cache/ck/zl.txt','a+')
        file4.write(str(zl))
        file5 = open('./cache/ck/tj.txt','a+')
        file5.write(str(tj))
    file3.close()
    file4.close()
    file5.close()
    return
    #运费
def yf():
    choose = input('1海运，2航空：')
    with open('./cache/ck/ysfs.txt','a+') as file:
        file.write(choose)
    tj = open('./cache/ck/tj.txt').read()
    zl = open('./cache/ck/zl.txt').read()
    if choose == '1':
        jzx1 = float(input('20集装箱单价：')) * 0.875 #有汇率
        jzx2 = float(input('40集装箱单价：')) * 0.875 #有汇率
        jzx3 = float(input('40h集装箱单价：')) * 0.875 #有汇率
        lclhc = float(input('LCL体积单价:')) * 0.875 #有汇率
        lclhm =  float(input('LCL重量单价：')) * 0.875 #有汇率
        with open('./cache/ck/jzx1.txt','a+') as file:
            file.write(str(jzx1))
        with open('./cache/ck/jzx2.txt','a+') as file:
            file.write(str(jzx2))
        with open('./cache/ck/jzx3.txt','a+') as file:
            file.write(str(jzx3))
        with open('./cache/ck/lclhc.txt','a+') as file:
            file.write(str(lclhc))
        file = open('./cache/ck/lclhm.txt','a+')
        file.write(str(lclhm))
    else:
        msc = float(input('最低运费msc:'))/float(100) * 0.875 #有汇率
        awc = float(input('AWC操作费：'))
        myc = float(input('MYC燃油费:')) /float(100) * 0.875 #有汇率
        with open('./cache/ck/myc.txt','a+') as file:
            file.write(str(myc))
        with open('./cache/ck/awc.txt','a+') as file:
            file.write(str(awc))
        with open('./cache/ck/msc.txt','a+') as file:
            file.write(str(msc))
        cbm = tj * float(167)
        hkzl = max(zl,cbm)
        with open('./cache/ck/htzl.txt','a+') as file:
            file.write(str(hkzl))
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
        file = open('./cache/ck/yunjia.txt','a+')
        file.write(str(yunjia))
    file.close()
    return
def cgcb():
    gcjg = float(input('工厂价格:'))
    ts = float(input('退税率:')) / 100
    zzs = float(input('增值税：'))/100
    with open('./cache/ck/zzs.txt','a+') as file:
        file.write(str(zzs))
    with open('./cache/ck/gcjg.txt','a+') as file:
        file.write(str(gcjg))
    with open('./cache/ck/ts.txt','a+') as file:
        file.write(str(ts))
    #检疫费用
    jy = input('有无检疫费用1有/2无：')
    with open('./cache/ck/ckjy.txt','a+') as file:
        file.write(str(jy))
