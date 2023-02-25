# 练习：根据身高体重，参照BMI，返回身体状况。
# BMI：用体重千克数除以身高米数的平方得出的数字
# 中国参考标准
# 体重过低BMI<18.5
# 正常范围18.5~24
# 超重24~28
# I度肥胖28~30
# II度肥胖30~40
# III度肥胖 BMI>=40

weight = float(input("请输入体重（千克）"))
height = float(input("请输入身高（米）"))

bmi = weight / height ** 2

if bmi < 18.5:
    print("体重过低")
elif bmi < 24:
    print("正常范围")
elif bmi < 28:
    print("超重")
elif bmi < 30:
    print("I度肥胖")
elif bmi < 40:
    print("II度肥胖")
else:
    print("III度肥胖")
