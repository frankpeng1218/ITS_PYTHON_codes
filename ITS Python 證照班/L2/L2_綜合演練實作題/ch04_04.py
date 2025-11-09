sum=0
for i in range(0,101):
    if (i%3==0 or i%7==0):
        sum += i
print("數值 1~100 中，所有是 3 或 7 倍數的數之總和 =",sum)  