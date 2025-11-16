def kgtolb(kg): 
    lb = kg * 2.2
    return lb

inputc = float(input("請輸入體重公斤數："))
print("你的體重為：%5.1f 磅" % kgtolb(inputc))