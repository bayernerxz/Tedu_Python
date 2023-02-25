"""
5．群讨论︰is与==的区别
"""

list01 = [1, 2, 3]
list02 = [1, 2, 3]

print(list01 == list02)  # True
print(list01 is list02)  # False

str01 = "abc"
str02 = "abc"

print(str01 == str02)  # True
print(str01 is str02)  # True

t01 = (1, 2)
t02 = (1, 2)

print(t01 == t02)  # True
print(t01 is t02)  # True

dict01 = dict(a=1, b=1)
dict02 = dict(a=1, b=1)

print(dict01 == dict02)  # True
print(dict01 is dict02)  # False

set01 = set("abc")
set02 = set("abc")

print(set01 == set02)  # True
print(set01 is set02)  # False

frozenset01 = frozenset("abc")
frozenset02 = frozenset("abc")

print(frozenset01 == frozenset02)  # True
print(frozenset01 is frozenset02)  # False
