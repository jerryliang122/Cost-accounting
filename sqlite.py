import sqlite3
import os
#sqlit检查目录下是否有文件
sql = os.path.exists('sql.db')
if not sql:
    conn = sqlite3.connect('sql.db')
    c = conn.cursor()
    c.execute('CREATE TABLE `Fixed value`( `name` TEXT NULL , `Value` TEXT NULL );')
    c.execute('CREATE TABLE `Calculated value`( `name` TEXT NULL , `Value` TEXT NULL );')
else:
    conn = sqlite3.connect('sql.db')
    c = conn.cursor()
    c.execute('DROP TABLE `Calculated value`;')
#完成数据库初始化
