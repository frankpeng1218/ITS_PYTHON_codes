scores = []
total =  0
for i in range(1,6):
    inscore = int(input("請輸入第 " + str(i) + " 同學的成績："))
    # 將成績加入 scores 串列中
    scores.append(inscore)

for score in scores:  # 將成績累加
    total += score
average = total / (len(scores))  #求平均值
print("本班總成績：%d 分，平均成績：%5.2f 分" % (total, average))