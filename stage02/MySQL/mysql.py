"""
pymysql.py
pymysql 操作数据库基本流程演示
"""

import pymysql

# 连接数据库
db = pymysql.connect(host="localhost", port=3306, user="root", password="123456", database="stu", charset="utf8")

# 获取游标（操作数据库，执行sql语句）
cur = db.cursor()

# 执行sql语句
sql = "insert into class values (8,'emma',17,'w',76.5,'2019-8-8');"  # 再pymysql模块中最后的;可以不加

cur.execute(sql)  # 执行语句

db.commit()  # 将写操作提交，读操作不需要，多次写操作一同提交也可以

# 关闭数据库
cur.close()
db.close()
