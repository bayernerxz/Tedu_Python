"""
    str字面值
    转义符：改变原始字符含义的符号
"""

name = "苏大强"
name = '苏大强'

# 可见即所得
name = '''苏大强'''
name = """
            苏
            大
            强
"""
print(name)

# 单引号内的双引号不算结束符
msg = '我叫"苏大强"'
# 双引号内的单引号不算结束符
msg = "我叫'苏大强'"

# 转义符：
msg = "我叫\"苏大强\""
msg = "我叫\n苏大强"  # 换行
msg = "我叫\t苏大强"  # 水平制表格tab键

url = "C:\\Users\\ASUS\\Documents\\Sports Interactive"
# 原始字符串(没有转义符)
url = r"C:\Users\ASUS\Documents\Sports Interactive"

# 字符串格式化
a = "1"
b = "2"
# "请输入" + str(a) + "+" + str(b) + "=?"

# 在字符串中插入变量
# 请输入1+2=？
# 字符串拼接（缺点：乱）
str01 = "请输入" + a + "+" + b + "=?"
str02 = "请输入%s+%s=?" % (a, b)
str03 = "请输入%s+%.1f=?" % ("1", 10.5678)
