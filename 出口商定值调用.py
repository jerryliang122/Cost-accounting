import os
import math
#成交数量
def cjsl():
    global zl
    global tj
    cjsl = input('成交数量:')
    baozhuangsldj = input('包装数量(转换到销售数量):')
    djbaozhuangzl=input('包装单件重量:')
    djbaozhuangtj=input('包装单件体积：')
    zl = float(djbaozhuangzl)/float(baozhuangsldj) * float(cjsl)
    tj = float(djbaozhuangtj)/float(baozhuangsldj) * float(cjsl)
    file2 =open('./cache/jk/djbaozhuangzl.txt','a+')
    file2.write(djbaozhuangzl)
    file3 =open('./cache/jk/djbaozhuangtj.txt','a+')
    file3.write(djbaozhuangtj)
    file4 = open('./cache/jk/zl.txt','a+')
    file4.write(str(zl))
    file5 = open('./cache/jk/tj.txt','a+')
    file5.write(str(tj))
    file2.close()
    file3.close()
    file4.close()
    file5.close()
    return
    #运费
def yf():
    choose = input('1海运，2航空：')
    file = open('./cache/ck/ysfs.txt','a+')
    file.write(choose)
    file.close()
    cjsl()
    if choose == '1':
        jzx1 = float(input('20集装箱单价：')) * 0.875
        jzx2 = float(input('40集装箱单价：')) * 0.875
        jzx3 = float(input('40h集装箱单价：')) * 0.875
        lclhc = float(input('LCL体积单价:')) * 0.875
        lclhm =  float(input('LCL重量单价：')) * 0.875
        file = open('./cache/ck/jzx1.txt','a+')
        file.write(jzx1)
        file.close()
        file = open('./cache/ck/jzx2.txt','a+')
        file.write(jzx2)
        file.close()
        file = open('./cache/ck/jzx3.txt','a+')
        file.write(jzx3)
        file.close()
        file = open('./cache/ck/lclhc.txt','a+')
        file.write(lclhc)
        file.close()
        file = open('./cache/ck/lclhm.txt','a+')
        file.write(lclhm)
        file.close()
    else:
        msc = float(input('最低运费msc:'))/float(100) * 0.875
        awc = float(input('AWC操作费：'))
        myc = float(input('MYC燃油费:')) /float(100) * 0.875
        file = open('./cache/ck/myc.txt','a+')
        file.write(myc)
        file.close()
        file = open('./cache/ck/awc.txt','a+')
        file.write(awc)
        file.close()
        file = open('./cache/ck/msc.txt','a+')
        file.write(msc)
        file.close()
        cbm = tj * float(167)
        hkzl = max(zl,cbm)
        file = open('./cache/ck/htzl.txt','a+')
        file.write(str(hkzl))
        file.close()
        if hkzl < float(45):
            yunjia = input('小于45运价：')
            file = open('./cache/ck/yunjia.txt','a+')
            file.write(str(yunjia))
            file.close()
        elif hkzl >= float('45') and hkzl < float('100'):
            yunjia = input('45-100运价:')
            file = open('./cache/ck/yunjia.txt','a+')
            file.write(str(yunjia))
            file.close()
        elif hkzl >= float('100') and hkzl < float('300'):
            yunjia = input('100-300运价:')
            file = open('./cache/ck/yunjia.txt','a+')
            file.write(str(yunjia))
            file.close()
        elif hkzl >= float('300') and hkzl < float('500'):
            yunjia = input('300-500运价:')
            file = open('./cache/ck/yunjia.txt','a+')
            file.write(str(yunjia))
            file.close()
        elif hkzl >= float('500') and hkzl < float('1000'):
            yunjia = input('500-1000运价:')
            file = open('./cache/ck/yunjia.txt','a+')
            file.write(str(yunjia))
            file.close()
        else:
            yunjia = input('1000以上运价:')
            file = open('./cache/ck/yunjia.txt','a+')
            file.write(str(yunjia))
            file.close()
    return