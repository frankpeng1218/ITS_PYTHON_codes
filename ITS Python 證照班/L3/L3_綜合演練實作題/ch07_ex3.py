import time as t

time1 = t.localtime()
show = "現在時刻："
if time1.tm_hour < 12: 
    show += "上午 "
    hour = time1.tm_hour
else:
    show += "下午 "
    hour = time1.tm_hour - 12
show += str(hour) + " 點 " + str(time1.tm_min) + " 分 "
show += str(time1.tm_sec) + " 秒"
print(show)
