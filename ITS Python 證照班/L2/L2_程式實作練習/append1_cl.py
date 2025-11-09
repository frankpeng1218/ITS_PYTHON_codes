moneys = []
total = money = 0
for i in range(1,8):
    money = int(input("請輸入第 " + str(i) + " 天的存款："))
    moneys.append(money) # 將存款加入 moneys 串列中

for money in moneys:  # 將存款累加
    total += money
print("存款總額：%d 元" % (total))
