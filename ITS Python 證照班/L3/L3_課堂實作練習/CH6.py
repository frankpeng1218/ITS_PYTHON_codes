# CH6 字典

# 重點複習 P6-2 ~ 6-3
#------------------------#
# 建立字典的方式
##dict_1 = {"frank": "honest", "Apple": 100}
##print(dict_1)
##
##dict_2 = dict([["frank", "honest"], ["Apple", 100]])
##print(dict_2)
##
##dict_3 = dict(frank="honest", Apple=100)
##print(dict_3)
#------------------------#

# 重點複習 P6-3
#------------------------#
# 字典取值
##dict_4 = {"frank": "honest", "Apple": 100}
##print(dict_4["frank"])
##print(dict_4["Apple"])
#------------------------#

# 重點複習 P6-4 ~ 6-5
#------------------------#
# 字典的鍵不存在
##dict_5 = {"frank": "honest", "Apple": 100}
### print(dict_5["Banana"]) # error
### 找字典是否有這個key
##print(dict_5.get("Amy")) # 如果沒有"Amy"這個key的話,會印出"None"
##print(dict_5.get("Amy", "找不到"))# 如果沒有"Amy"這個key的話,會印出"找不到"
#------------------------#

# 重點複習 P6-6
#------------------------#
# 字典維護
# 修改value的方式
##dict_6 = {"frank": "honest", "Apple": 100}
##print("原本的:", dict_6)
##dict_6["Apple"] = 200
##print("後來的:", dict_6)
##
### 新增key-value的方式
##dict_7 = {"frank": "honest", "Apple": 100}
##print("原本的:", dict_7)
##dict_7["Amy"] = "Frank's GF"
##print("後來的:", dict_7)

# 刪除的方式
##dict_8 = {"frank": "honest", "Apple": 100}
##print("原本的:", dict_8)
##del dict_8["Apple"]
##print("後來的:", dict_8)
### clear()
##print("原本的:", dict_8)
##dict_8.clear()
##print("後來的:", dict_8)
### del 整個字典
##print("原本的:", dict_8)
##del dict_8
##print("後來的:", dict_8) # error 因為你已經刪掉了
#------------------------#

# 重點複習 P6-8
#------------------------#
# 檢查「鍵」是否存在
##dict_9 = {"frank": "honest", "Apple": 100}
##if "Apple" in dict_9:
##    print("Yes Apple是dict_9的key")
##else:
##    print("No Apple不是dict_9的key")
### 取得以「鍵」為元素的組合
### 取得「值」為元素的組合
##print(dict_9.keys())
##print(dict_9.values())
#------------------------#

# 重點複習 P6-8 ~ 6-9
#------------------------#
# 檢查字典中的「鍵」是否存在
dict_10 = {"frank": "honest", "Apple": 100}
print("Apple" in dict_10)
print("Amy" in dict_10)


