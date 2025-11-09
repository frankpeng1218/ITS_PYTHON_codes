scores = []
names= []
for i in range(1,4):
    name = input("請輸入第 " + str(i) + " 同學的姓名：")
    inscore = int(input("請輸入第 " + str(i) + " 同學的成績："))
    # 將姓名、成績加入 names、scores 串列中
    names.append(name)
    scores.append(inscore)    
scores2=sorted(scores,reverse=True) # 由大到小排序 
# 取得最大數在 scores 串列的索引位置
n = scores.index(scores2[0])  
print("姓名： %s    成績： %d" %(names[n],scores[n])) 