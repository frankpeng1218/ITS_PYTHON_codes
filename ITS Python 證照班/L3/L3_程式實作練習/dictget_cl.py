dict1 = {"春季":"暖和", "夏季":"炎熱", "秋季":"涼爽", "冬季":"寒冷"}
name = input("輸入季節名稱:")
feeling = dict1.get(name)
if feeling == None:  
    print("沒有「" + name + "」季節！")
else:  
    print(name + "的天氣為 " + str(dict1[name]))