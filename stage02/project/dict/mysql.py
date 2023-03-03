"""
数据库操作模块
思路：
将数据库操作封装一个类，将dict_server需要的数据库操作
功能分别携程方法，在dict_server中实例化对象，需要什么方法直接调用
"""

import pymysql
import hashlib

SALT = "#&Aid_"  # 密码加盐的密钥


class Database:
    def __init__(self, host="localhost", port=3306, user="root",
                 passwd="123456", charset="utf8", database=None):
        self.host = host
        self.port = port
        self.user = user
        self.passwd = passwd
        self.database = database
        self.charset = charset
        self.db = pymysql.connect(host=self.host, port=self.port, user=self.user, passwd=self.passwd,
                                  database=self.database, charset=self.charset)  # 链接数据库

    # 关闭数据库
    def close(self):
        self.db.close()

    # 创建游标
    def create_cursor(self):
        # 这里因为需要每个子进程创建时都需要分别创建一个游标对象，所以需要在这里创建游标对象
        self.cur = self.db.cursor()

    # 注册操作
    def register(self, name, passwd):
        sql = "select * from user where name='%s'" % name
        self.cur.execute(sql)
        r = self.cur.fetchone()
        # 查找到则用户存在
        if r:
            return False

        # 密码加密存储处理
        hash = hashlib.md5((name + SALT).encode())  # 加盐密码
        hash.update(passwd.encode())  # 算法加密
        passwd = hash.hexdigest()  # 加密后的密码

        # 插入数据库
        sql = "insert into user (name,passwd) values (%s,%s)"
        try:
            self.cur.execute(sql, [name, passwd])
            self.db.commit()
            return True
        except Exception:
            self.db.rollback()
            return False

    # 登录
    def login(self, name, passwd):
        # 密码加密存储处理
        hash = hashlib.md5((name + SALT).encode())  # 加盐密码
        hash.update(passwd.encode())  # 算法加密
        passwd = hash.hexdigest()  # 加密后的密码

        # 数据库查找
        sql = "select * from user where name='%s' and passwd='%s'" % (name, passwd)
        self.cur.execute(sql)
        r = self.cur.fetchone()
        # 有数据允许登录
        if r:
            return True
        else:
            return False

    # 查单词
    def query(self, word):
        sql = "select mean from words where word='%s'" % word
        self.cur.execute(sql)
        r = self.cur.fetchone()
        # 如果找到r --> (mean)
        if r:
            return r[0]

    # 插入历史记录
    def insert_hist(self, name, word):
        sql = "insert into hist (name,word) values (%s,%s)"
        try:
            self.cur.execute(sql, [name, word])
            self.db.commit()
        except Exception:
            self.db.rollback()

    # 历史揭露
    def history(self, name):
        sql = "select name,word,time from hist where name='%s' order by time limit 10" % name
        self.cur.execute(sql)
        return self.cur.fetchall()
