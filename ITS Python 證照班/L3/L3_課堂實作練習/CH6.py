# CH6 字典

# 重點複習 P6-2 ~ 6-3
#------------------------#
##dict_1 = {"frank": "坦率的", "Apple": "蘋果",
##          "banana": 50, "cherry": 100.3,
##          "train": [1, 4, 6], "Yes": True,
##          "dict123": {"frank": "超帥", "承諺": False}}
##print(dict_1)
##
##dict_2 = dict([["frank", "帥哥"], ["雨翔", "小帥哥"]])
##print(dict_2)
##
##dict_3 = dict(frank="帥哥", 雨翔="小帥")
##print(dict_3)

#------------------------#
# 重點複習 字典取值 P6-3
##dict_4 = {"frank": "坦率的", "Apple": 123}
##print(dict_4["frank"])
##print(dict_4["Apple"])

#------------------------#
# 重點複習 字典的鍵不存在 P6-4 ~ 6-5
##dict_5 = {"frank": "坦率的", "Apple": 123}
### print(dict_5["Henry"]) # error
##print(dict_5.get("Henry", "找不到")) # 找字典有沒有"Henry"


#------------------------#
# 重點複習 字典維護 P6-6
# 修改值的方式
##dict_6 = {"Apple": 20, "Banana": 30, "Dragonfruit": 60}
##print("原本Apple的價錢:", dict_6["Apple"])
##dict_6["Apple"] = 120
##print("後來Apple的價錢:", dict_6["Apple"])
### 新增key-value的方式
##print("原本的dict_6:", dict_6)
##dict_6["Cherry"] = 200
##print("新增Cherry後的dict_6:", dict_6)


#------------------------#
# 重點複習 字典維護 P6-7
# 刪除的方式
##dict_7 = {"Apple": 20, "Banana": 30, "Dragonfruit": 60}
##print("刪除前:", dict_7)
##del dict_7["Banana"]
##print("刪除後:", dict_7)
##
### clear()
##dict_7.clear()
##print("clear()後:", dict_7)
##
### del整個字典
##del dict_7
##print("del 整個字典後:", dict_7) # Nameerror因為被刪掉了

#------------------------#
# 重點複習 字典進階操作 P6-8
# 檢查「鍵」是否存在
dict_8 = {"Apple": 20, "Banana": 30, "Dragonfruit": 60}
if "Apple" in dict_8:
    print("Apple是dict_8的key")
else:
    print("Apple不是dict_8的key")

# 取得以「鍵」為元素的組合
print(dict_8.keys())
# 取得「值」為元素的組合
print(dict_8.values())

# 重點複習 字典進階操作 P6-8 ~ 6-9
print("Apple" in dict_8)
print("Cindy" in dict_8)












