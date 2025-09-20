height = float(input("請輸入您的身高(cm)："))
weight = float(input("請輸入您的體重(kg)："))
bmi = weight / (height/100)**2
print("身高 %d 公分，體重 %d 公斤，BMI值為 %.2f" % (height, weight, bmi))