# CH7 函式與模組
# 重點複習 P7-2 ~ 7-3
#------------------------#
# 沒有參數傳入，也沒有回傳值
##def SayGood():
##    print("Frank is good!")
##SayGood()
### 有參數輸入, 有一個回傳值
##def add(a, b):
##    c = a + b
##    return c
##result = add(2, 3)
##print(result)
### 有參數輸入, 有多個回傳值
##def circle(radius):
##    area = radius*radius*3.14 # 面積
##    perimeter = 2*radius*3.14 # 周長
##    return area, perimeter
##
##result_area, result_perimeter = circle(3)
##print(result_area)
##print(result_perimeter)
#------------------------#

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
#------------------------#

# 重點複習 P7-7
#------------------------#
# 常見的內建函式
##x = 5
##print(float(x))
##x = "10"
##print(int(x))
##x = [1, 3, 5]
##print(len(x))
##x = 4.88
##print(round(x))
##x = 123
##print(str(x))
##x = 2
##y = 5
##print(pow(x, y))# x的y次方, x=2, y=5->2*2*2*2*2 = x**y
##x = 10
##y = 3
##print(divmod(x, y)) #(10//3, 10%3)
##s = "A"
##print(ord(s)) # 65
##c = 65
##print(chr(c)) # "A"

# 數值函式 - 補充
### round(x)
##print(round(1.4)) # 1
##print(round(1.6)) # 2
##print(round(1.5)) # 2
##print(round(2.5)) # 2
##print(round(3.5)) # 4
##
##import math
### ceil, floor
##print(math.ceil(1.1)) # 無條件進位
##print(math.floor(2.999999))# 無條件捨去
#------------------------#

# 重點複習 P7-13
#------------------------#
# 常用的字串函式
# find()
##text_1 = "Frank is handsome"
##result_1 = text_1.find("is") # index的位置
##result_2 = text_1.find("handsome") # index的位置
##print(result_1)
##print(result_2)

# len()
##text_2 = "Frank is super good"
##lengh = len(text_2)
##print(lengh)

# replace(s1, s2)->用s2取代s1
##text_3 = "Frank is super good"
##result = text_3.replace("good", "ugly")
##print(result)

# split() # 把字串變成串列
##text_4 = "a b c d"
##result = text_4.split() # 以空格分開"a b c d"->["a", "b", "c", "d"]
##print(result)
##text_5 = "1@2@3@4"
##result = text_5.split("@")# 以@分開"1@2@3@4"->["1", "2", "3", "4"]
##print(result)
##text_6 = "1@2@3@4"
##result = text_6.split("3")# 以3分開"1@2@3@4"->["1@2@", "@4"]
##print(result)
#------------------------#

# 重點複習 P7-14
#------------------------#
# 連接與分割字串
# join() # 把串列組成字串
##list_eg = ["1", "3", "5", "7"]
##text_eg = "!!!".join(list_eg)
##print(text_eg)
#------------------------#

# 重點複習 P7-22 ~ 7-23
#------------------------#
# random
##import random as fkkkk
##a = fkkkk.randint(1, 10) # 可能1~10
##print(a)

##import random
##a = random.randint(1, 10) # 可能1~10
##print(a)
##
##b = random.randrange(1, 10) # 可能1~9
##print(b)
##c = random.randrange(0, 10, 2) # 可能0, 2, 4, 6, 8
##print(c)
##
##d = random.random() # 0~1之間的浮點數(不包含1)
##print(d)
##
##e = random.uniform(1, 5) # 1~5之間的浮點數(包含5)
##print(e)
#------------------------#

# 重點複習 P7-27 ~ 7-28
#------------------------#
# 隨機取得字元或串列元素
##import random
##text_1 = "ABCD"
##a = random.choice(text_1)
##print(a)
##list_1 = ["Frank", "Amy", "Daniel"]
##b = random.choice(list_1)
##print(b)
##
##c = random.sample(text_1, 2)
##print(c)
##d = random.sample(list_1, 2)
##print(d)
#------------------------#

# 重點複習 P7-30
#------------------------#
import time
##start = time.perf_counter() # 也可以使用time.time()
##for i in range(100000):
##    pass
##end = time.perf_counter() # 也可以使用time.time()
##print("執行時間: ", end-start)

##t = time.time()
##print("t: ", t)
##ctime = time.ctime(t)
##print("看得懂的時間: ", ctime)
##
##t = time.time()
##result = time.localtime(t)
##print("localtime: ", result)

print(123)
time.sleep(3)
print(456)












    
