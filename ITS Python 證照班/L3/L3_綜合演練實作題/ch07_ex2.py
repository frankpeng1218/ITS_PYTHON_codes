def fttocm(ft): 
    cm = ft * 0.3048 * 100
    return cm

inputc = float(input("請輸入身高 (呎) ："))
print("你的身高為：%5.1f 公分" % fttocm(inputc))