# CH4 迴圈

# 重點複習 P4-2 ~ 4-3
#------------------------#
# range(x, y, z): x 是起點, y 是終點(不包含), z 是間隔
#------------------------#

a = list(range(10))  # range(10) 等同於 range(0, 10, 1)
print(a)

b = list(range(5, 9))  # range(5, 9) = [5, 6, 7, 8]
print(b)

c = list(range(1, 7, 2))  # range(1, 7, 2) = [1, 3, 5]
print(c)

#------------------------#
# for 迴圈搭配 range() 使用
#------------------------#

for p in range(-3, 7):  # 從 -3 印到 6
    print(p)

for k in range(-2, 10, 5):  # 從 -2 開始，每次加 5，直到小於 10
    print(k)

for l in range(7, 3):  # 由於沒有指定負間隔，所以不會執行
    print(l)

#------------------------#
# 重點複習 P4-8：巢狀迴圈
#------------------------#

for x in range(5):
    print("*")  # 外層每次印出 *
    for y in range(3):
        print("Q")  # 內層每次印出 Q 三次

#------------------------#
# 隨堂練習 04：利用巢狀迴圈印出圖案
#------------------------#

for i in range(1, 5 + 1):  # 外層控制列數，共 5 列
    for j in range(0, i):  # 每列前面印出 i 個空白
        print(" ", end="")
    for j in range(i, 5 + 1):  # 再印出剩下的星號
        print("*", end="")
    print()  # 換行

#------------------------#
# 重點複習 P4-11 ~ 4-12：break 的使用
#------------------------#

a = 2
while a < 10:
    print("a =", a)
    a += 1
    if a == 5:
        break  # 當 a == 5 時跳出 while 迴圈

for i in range(1, 10):
    print("i =", i)
    if i > 5:
        break  # 當 i > 5 時跳出 for 迴圈

#------------------------#
# continue 的使用
#------------------------#

a = 2
while a < 10:
    print("a =", a)
    a += 1
    if a == 5:
        continue  # 略過下面程式，直接進入下一次迴圈
    print("沒有continue")

for i in range(1, 10):
    if i > 3:
        continue  # 略過 i > 3 的情況
    print("i =", i)

#------------------------#
# 重點複習 P4-14 ~ 4-15
# 使用 control + c 中斷無限迴圈
#------------------------#

# 例如：
# while True:
#     print("這是無限迴圈，請按 Ctrl + C 結束")
