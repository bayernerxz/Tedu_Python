"""
逆波兰表达式练习
"""

from sstack import *


def logic_process(list_):
    for item in list_:
        if item.isdigit() is True:
            st.push(int(item))
        if is_float(item) is True:
            st.push(float(item))
        if item in operator:
            handle_operator(item)
        if item == "p":
            print(st.top())
        if item == "q":
            exit()


def handle_operator(operator_):
    exec("num1 = st.pop()")
    exec("num2 = st.pop()")
    exec("result = num2 %s num1" % operator_)
    exec("st.push(result)")


def is_float(string):
    tmp = string.split(".")
    if len(tmp) > 3 or len(tmp) == 0:
        return False
    else:
        for item in temp_list:
            if item.isdigit() is False:
                return False
        return True


st = SStack()
operator = ["+", "-", "*", "/", "//", "**"]

while True:
    str_operate = input("请输入字符：")
    temp_list = str_operate.split(" ")

    logic_process(temp_list)
