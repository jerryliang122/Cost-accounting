import sqlite3
import os

conn = sqlite3.connect("sql.db")
c = conn.cursor()
#完成数据库连接

#写入数据
def setdata(data,name,value):
    c.execute(f"INSERT INTO '{data}'('name','value') VALUES ('{name}','{value}')")
    conn.commit()
    conn.close()
    return
#读取数据
def readdata(data,name):
    i = c.execute(f"SELECT * from '{data}' WHERE name='{name}'").fetchall()
    conn.close()
    i =str(i)
    i = i.split(',')
    i = i[1].split("'")
    i = i[1]
    return i
#更新数据
def updatedata(data,name,value):
    c.execute(f"update '{data}' set value = '{value}' where name = '{name}'")
    conn.commit()
    conn.close()
    return
#删除数据
def deldata(data,name,value):
    c.execute(f"delete from '{data}' where name = '{name}'")
    conn.commit()
    conn.close()
    return