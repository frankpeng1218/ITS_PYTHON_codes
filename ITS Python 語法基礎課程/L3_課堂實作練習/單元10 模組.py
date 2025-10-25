# 單元10 模組

#------------------------#
# 模組-載入與使用模組
import random
rand = random.randrange(10) #產生 0-9 的隨機整數print(rand)
#----------------#
# 模組-亂數模組的 randrange() 函式
import random
random.randrange(10) #產生 0-9 的隨機整數
random.randrange(100) #產生 0-99 的隨機整數
random.randrange(10, 20) #產生 10-19 的隨機整數
random.randrange(20, 100) #產生 20-99 的隨機整數
random.randrange(10, 30, 2) #10, 12, 14, ... 28 隨機挑一個數值，不包含 30
random.randrange(50, 100, 5) #50, 55, 60, ... 95 隨機挑一個數值，不包含 100
#----------------#
# 模組-亂數模組的 random() 函式
import random
random.random() #產生 0-1 的隨機小數
random.random()*100 #產生 0-100 的隨機小數
random.random()*100 + 50 #產生 50-150 的隨機小數
#----------------#
# 模組-載入模組的指定函式
from random import randrange
a = randrange(10)
b = randrange(50)
c = randrange(100)
print(a, b, c)

from random import *
a = randrange(10)
b = random()
print(a, b)
#----------------#
# 模組-時間模組 time, time 函式
import time
print(time.time()) #產生時間數值
#----------------#
# 模組-ctime 函式
import time
print(time.ctime()) #星期 月份 日數 小時:分鐘:秒數 西元年
#----------------#
# 模組-sleep 函式
import time
print("再等我5秒鐘就好!")
time.sleep(5)
print("我好了! 出發吧!")
#----------------#
























