"""
将1970年到2050年中的闰年，存入列表
"""
# list_leap_years = []
# for i in range(1970, 2051):
#     if i % 4 != 0:
#         continue
#     elif i % 100 == 0 and i % 400 != 0:
#         continue
#     list_leap_years.append(i)

list_leap_years = [item for item in range(1790, 2051) if item % 4 == 0 and item % 100 != 0 or item % 400 == 0]

print(list_leap_years)
