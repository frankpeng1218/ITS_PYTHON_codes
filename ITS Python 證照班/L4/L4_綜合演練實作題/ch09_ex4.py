try:
    n=int(input("請輸入正整數 n："))
    for i in range(1,n+1):
        print(i,end=" ")
except:
    print("發生輸入非數值的錯誤!") 