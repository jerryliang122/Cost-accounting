import sqlite3
import os

#sqlit检查目录下是否有文件
sql = os.path.exists('sql.db')
if not sql:
    conn = sqlite3.connect('sql.db')
    c = conn.cursor()
    c.execute('CREATE TABLE `fixed value`( `name` TEXT NULL , `value` TEXT NULL );')
    c.execute('CREATE TABLE `calculated value`( `name` TEXT NULL , `Value` TEXT NULL );')
    conn.commit()
else:
    conn = sqlite3.connect('sql.db')
    c = conn.cursor()
#完成数据库初始化 c.execute('DROP TABLE `calculated value`;')

#写入数据
def setdata(data,name,value):
    c.execute(f'INSERT INTO {data}({name}) VALUES{value}')
    conn.commit()
    c.close()
    return
#读取数据
def readdata(data,name):
    i = c.execute(f'SELECT * from {data} WHERE name={name}').fetchall()
    c.close()
    i =str(i)
    return i
#更新数据
def updatedata(data,name,value):
    c.execute(f'update {data} set value = {value} where name = {name}')
    conn.commit()
    c.close()
    return
#删除数据
def deldata(data,name,value):
    c.execute(f'delete from {data} where name = {name}')
    return