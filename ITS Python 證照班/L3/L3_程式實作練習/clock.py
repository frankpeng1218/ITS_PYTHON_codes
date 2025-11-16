import time as t

timestart = t.clock()
for i in range (0,1000):
    for j in range (0,1000):
        n = i * j
timeend = t.clock()
print("執行一百萬次整數運算的時間：" + str(timeend-timestart) + " 秒")
