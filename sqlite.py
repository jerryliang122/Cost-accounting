import sqlite
import os
#sqlit检查目录下是否有文件
sql = os.path.exists('sql.db')
if not sql:
     