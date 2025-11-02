# CH2 變數與運算式

# 重點複習P2-3~2-4
#------------------------#
# 多變數一起定義一個值
x = y = z = 20

print(x)
print(y)
print(z)

# 多個變數多個值
apple, banana, name = 100, 20, "Frank"

print(apple)
print(banana)
print(name)

# 刪除變數
score = 100
del score

print(score)
#----------------#


# 重點複習P2-5
#------------------------#
# 註解
name = "Frank" # 定義一個變數內容是"Frank"

# 三個單引號
'''
Frank老師是一個小帥哥
'''

# 三個雙引號
"""
Frank老師人非常好
"""
#----------------#


# 重點複習P2-6~P2-7
#------------------------#
# 資料型態
a = 10
b = 8.7
c = True # 數字時視為1
d = False # 數字時視為0

print(a+b)
print(a+c)
print(b-d)

# 跳脫字元 "\"
print("\'")
print("\"")
print("\t", 123, "\n")
#----------------#

# 重點複習P2-8
#------------------------#
# 資料型態轉換
num1 = 5 + 7.8
# 錯誤: num2 = 23 + "67"
num3 = 23 + int("67")
#----------------#

# 重點複習P2-9
#------------------------#
# 輸出與輸入
print("orange", "apple") # 預設是sep=" ", end="\n"
print("oragne", "apple", sep="+")
print("oragne", "apple", end="!")
#----------------#

# 重點複習P2-9~2-10
#----------------#
# 「%」字串格式化
name = "Frank"
score = 200
print("%s 的成績為 %d"% (name, score))

money = 100
print("My cash = %5d" % money) # 多餘的左邊補空白
name = "Frank"
print("My name is %5s" % name) # 多餘的左邊補空白, 少的則忽略, %2s還是會印出Frank
price = 23.8
print("The price is %8.2f" % price)
#----------------#

# 重點複習P2-11~2-12
#----------------#
# format 格式化
name = "Frank"
money = 78
print("{:5s}有{:.2f}元".format(name, money))

# [補充] f-string
name = "Frank"
age = 18
print(f"My name is {name}, {age} years old")
#----------------#

# 重點複習P2-13
#----------------#
# input 輸入命令
# number = int(input()) # 都會是字串
# print(f"剛剛輸入的是:{number}")
#----------------#


# 重點複習P2-16
#----------------#
# 算數運算子
a = 10//3 # 只取整數的商
b = 10%3
c = 10/3
d = 2**3

# 比較運算子
e = 5==3
print(f"==:{e}")
f = 5!=3
print(f"!=:{f}")
g = 5>3
print(f"> :{g}")
h = 5>=3
print(f">=:{h}")

# 邏輯運算子
i = not True
print(f"not:{i}")
j = (5>3) or (6>=8)
print(f"or:{j}")
k = (5>3) a