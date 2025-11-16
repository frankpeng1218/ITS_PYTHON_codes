# CH7 函式與模組
# 重點複習 P7-2 ~ 7-3
#------------------------#
# 沒有參數傳入，也沒有回傳值
##def SayGood():
##    print("You are good")
##SayGood()

# 有參數傳入，有一個回傳值
##def add(a, b):
##    c = a + b
##    return c
##result = add(7, 8)
##print(result)

# 有參數傳入，有多個回傳值
##def circle(radius):
##    area = radius*radius*3.14
##    perimeter = 2*radius*3.14
##    return area, perimeter
##
##result_area, result_perimeter = circle(5)
##print(result_area)
##print(result_perimeter)


# 重點複習 P7-5
#------------------------#
# 變數有效範圍
##a = 1 # global
##b = 1 # global
##c = 1 # global
##
##def add(a, b):
##    global c
##    sub(c+2)
##    c = a+b
##
##def sub(c):
##    global a, b
##    a = c-1
##    b += 3
##    print(a, b, c)
##
##print(a, b, c)
##a += 2
##add(c, a)
##print(a, b, c)


# 重點複習 P7-7
#------------------------#
##x = 5
##print(float(x))
##x = "10"
##print(int(x))
##x = [1, 4, 5]
##print(len(x))
##x = 4.88
##print(round(x))
##x = 123
##print(str(x))
##x = 2
##y = 3
##print(pow(x, y)) # x乘以y次的x, x = 2, y = 3->2*2*2
##
### 數值函式 - 補充
### 無條件進位
##import math
##x = 3.1
##print(math.ceil(x))
### 無條件捨去
##x = 3.99999
##print(math.floor(x))



# 重點整理 P7-13
#------------------------#
# 常用的字串函式
# find(s)
##text = "Frank is good"
##print(text.find("good")) # 9->index第9的地方出現good
##print(text.find("Happy")) # -1->沒這個東西

# len()
##text_a = "Frank is ugly"
##print(len(text_a))

# replace(s1, s2)
##text_b = "Frank is mean"
##print(text_b.replace("Frank", "Henry"))

# split(s)
##text_c = "a b c d"
##print(text_c.split()) # 以空格分開後就會變成list
##text_d = "1@2@3@4"
##print(text_d.split("@")) # 以逗號隔開->["1", "2", "3", "4"]


# 重點整理 P7-14
#------------------------#
# 連接與分割字串
##list_text = ["1", "2", "3", "4"]
##text_e = "@".join(list_text)
##print(text_e)


# 重點整理 P7-24
#------------------------#
# 常用的模組函式
##import random
##a = random.randint(1, 10) # 可能1~10
##print(a)
##
##b = random.randrange(1, 10) # 可能1~9
##print(b)
##c = random.randrange(0, 20, 2) # 可能0, 2, 4, 6...18
##print(c)
##
##d = random.random() # 0~1之間的浮點數
##print(d)
##
##e = random.uniform(1, 5)# 1~5之間的浮點數
##print(e)

# 重點整理 P7-27 ~ 7-28
#------------------------#
# 隨機取得字元或串列元素
##import random
##text_1 = "ABCDE"
##a = random.choice(text_1)
##print(a)
##list_1 = [1, 3, 5, 7, 9]
##b = random.choice(list_1)
##print(b)
##
##c = random.sample(text_1, 3)
##print(c)
##d = random.sample(list_1, 2)
##print(d)


# 重點複習 P7-30
#------------------------#
import time
##start = time.perf_counter() # 也可以使用time.time()
##for i in range(10000):
##    pass
##end = time.perf_counter() # 也可以使用time.time()
##print("執行時間: ", end-start)
##
##t = time.time()
##print(t)
##ctime = time.ctime(t)
##print(ctime)
##
##t = time.time()
##result = time.localtime(t)
##print(result)

print(123)
time.sleep(3)
print(456)



















