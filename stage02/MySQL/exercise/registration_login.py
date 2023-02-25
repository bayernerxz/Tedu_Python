import pymysql

PROMPT = "请输入1或2：\n1.注册\n2.登录\n"


def registration(database, cursor):
    name = input("Name:")
    password = input("password:")
    sql = "select name from user where name=%s"
    cursor.execute(sql, [name])
    if not cursor.fetchone():
        sql = "insert into user (name,password) values (%s,%s)"
        cursor.execute(sql, [name, password])
        database.commit()
    else:
        print("用户名已存在")


def login(database, cursor):
    name = input("Name:")
    password = input("password:")
    sql = "select name,password from user where name=%s"
    cursor.execute(sql, name)
    data = cursor.fetchone()
    if not data:
        print("用户名或密码输入错误，请重新输入")
        return False
    else:
        pswd = data[1]
        if pswd == password:
            print("登录成功")
            return True
        else:
            print("用户名或密码输入错误，请重新输入")
            return False


db = pymysql.connect(host="localhost", port=3306, user="root", passwd="123456", database="order_manage", charset="utf8")
cur = db.cursor()
while True:
    option = input(PROMPT)
    if option == "1":
        if registration(db, cur):
            break
    elif option == "2":
        if login(db, cur):
            break
    elif not "":
        print("输入有误，请重新输入")
    else:
        break
