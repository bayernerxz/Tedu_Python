"""
    *#*#*#
    *#*#*#
    *#*#*#
    *#*#*#
"""

for r in range(4):
    for c in range(6):
        if c % 2 == 0:
            print("*", end="")
        else:
            print("#", end="")

    print()
