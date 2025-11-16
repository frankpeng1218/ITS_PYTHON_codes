def change(n,coin): # 換硬幣
    m = n // coin   # 硬幣數
    return m    

money=[50,10,5,1]
n=int(input("請輸入換幣金額："))
while (n>0):
    for i in range(len(money)):
        coin = money[i]
        if (n >= coin):
            m = change(n,coin) # 換硬幣
            print("{}元 * {}個" .format(coin,m))
            n= n % coin