"""
    包

python程序结构
文件夹 -----项目根目录
    包
        模块
            类
                函数
                    语句
"""

# # 1. from 包.模块 import 成员
# from package01.module_a import fun01
#
# fun01()
#
# # 2. from 包.包.模块 import 成员
# from package01.package02.module_b import fun02
# fun02()


# import package01.module_a as pm
# pm.fun01()

# 3. 语法：from 包 import *
# 一般不这样用，上面两个用法为多。因为IDE只能指示包里的模块名，不能提示模块里的成员名。
# 依赖于在包的__init__.py文件中指定__all__=[可导出的模块]
# from package01 import *

# 4.在非pycharm环境中运行模块时，如果导入的包不在当前模块所在的项目根目录中，
# 需要手动增加需要导入包的目录进入sys.path中。
# import sys
#
# sys.path.append("C:/")
