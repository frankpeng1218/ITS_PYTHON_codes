innum = 0
list1 = []
for i in range(0,4):
    innum = int(input("請輸入第 " + str(i+1) + " 位同學分數："))
    list1.append(innum)
print("最高分為：%d" % max(list1))
print("最低分為：%d" % min(list1))
print("總分為：%d" % sum(list1))
print("平均為：%6.2f" % (sum(list1)/4))