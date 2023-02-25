"""
练习：将单词本存入数据库

1.创建数据库dict （utf8）
create database dict;
2.创建数据表 words 将单词和单词解释分别存入不同的字段。
create table words (id int primary key auto_increment,word varchar(32) not null, explanation text);
3.将单词存入words单词表
"""

import pymysql

db = pymysql.connect(host="localhost", port=3306, user="root", passwd="123456", database="dict", charset="utf8")
cur = db.cursor()
f = open("./dict2.txt", "r", encoding="utf-8")
while True:
    data = f.readline()
    if not data:
        break

    # 老师的做法
    # tmp = data.split(" ")
    # word = tmp[0]
    # explanation = " ".join(tmp[1:]).strip()

    # 正则表达式的做法
    # import re
    # word = re.findall("(^\S)\s+(.*)$")[0][1]
    # explanation = re.findall("(^\S)\s+(.*)$")[0][1]

    split_mark = data.find("   ")
    word = data[:split_mark]
    explanation = data[split_mark + 3:len(data) - 1]  # 因为每一行的最后一个字符是换行，所以少取一个
    sql = 'insert into words (word,explanation) values (%s,%s)'
    try:
        cur.execute(sql, [word, explanation])
    except Exception as e:
        db.rollback()
        print(e)
        continue
db.commit()

f.close()
cur.close()
db.close()
