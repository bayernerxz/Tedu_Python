"""
    列表推导式嵌套
"""

list01 = list("abc")
list02 = list("ABC")

list03 = []
for r in list01:
    for c in list02:
        list03.append(r + c)

print(list03)

list04 = [r + c for r in list01 for c in list02]

print(list04)
