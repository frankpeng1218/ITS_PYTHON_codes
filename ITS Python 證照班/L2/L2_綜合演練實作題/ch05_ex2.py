fruits = ["香蕉","蘋果","橘子","鳳梨","s"]
while True:
    fruit = input("請輸入喜歡的水果(Enter 結束)：")
    if (fruit==""):
        break
    n = fruits.count(fruit) 
    if (n>0):  # 串列元素存在
        p=fruits.index(fruit)
        print("%s 在串列中的第 %d 項" %(fruit,p+1))
    else:
        print(fruit,"不在串列中!")