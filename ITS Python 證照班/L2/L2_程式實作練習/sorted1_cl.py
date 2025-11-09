scores = []
while True:
    inscore = input("請輸入學生的成績：")
    if (inscore==""):
        break
    # 將成績轉為數值後加入 scores 串列中
    scores.append(int(inscore))  

scores2=sorted(scores,reverse=False) # 由小到大排序
print("成績由小到大排序：",scores2) 