# 练习:定义生成器函数my_zip,实现下列现象.
# 将多个列表的每个元素合成一个元组.
list02 = ["孙悟空", "猪八戒", "唐僧", "沙僧"]
list03 = [101, 102, 103, 104, 105]


# for item in zip(list02, list03):
#     print(item)

def my_zip(*containers):
    length_list = []
    for item in containers:
        length_list.append(len(item))

    for i in range(min(length_list)):
        element_list = []
        for item in containers:
            element_list.append(item[i])
        yield tuple(element_list)


for item in my_zip(list02, list03):
    print(item)
