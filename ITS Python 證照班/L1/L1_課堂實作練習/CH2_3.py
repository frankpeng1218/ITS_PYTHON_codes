# CH3 變數與運算式

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
k = (5>3) and (6>=8)
print(f"and:{k}")

# 複合指定運算子
a = 10
a = a + 1 # a+=1
print(f"a=:{a}")
b = 10
b = b * 2 # a*=2
print(f"b=:{b}")
#----------------#

# 重點複習P2-22
#----------------#
equation = 56 > 78 and 34 > (4+2) + 5*2
print(f"equation結果: {equation}")












