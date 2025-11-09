n = int(input("請輸入正整數："))
for i in range(1,n+1):
    for j in range(i,n+1):
        print("*", end="")
    print()
