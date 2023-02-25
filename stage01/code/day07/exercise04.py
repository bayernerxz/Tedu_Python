# 练习2：经理∶曹操，刘备，孙权
# 技术∶曹操，刘备，张飞，关羽
# 请计算:
# (1)是经理也是技术的有谁?
# (2)是经理，不是技术的有谁?
# (3)是技术，不是经理的有谁?
# (4 )张飞是经理吗?
# (5)身兼一职的都有谁?
# (6)经理和技术总共有都少人?
set_manager = {"曹操", "刘备", "孙权"}
set_tech = {"曹操", "刘备", "张飞", "关羽"}
# (1)是经理也是技术的有谁?
print(set_manager & set_tech)
# (2)是经理，不是技术的有谁?
print(set_manager - set_tech)
# (3)是技术，不是经理的有谁?
print(set_tech - set_manager)
# (4 )张飞是经理吗?
print("张飞" in set_manager)
# (5)身兼一职的都有谁?
print(set_manager ^ set_tech)
# (6)经理和技术总共有都少人?
print(len(set_manager | set_tech))
