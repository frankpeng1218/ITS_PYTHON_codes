try:
    n=int(input("請輸入正整數 n："))
    for i in range(1,n+1):
        print(i,end=" ")
except Exception as e:
    print("發生錯誤的原因：" , e)     
    
''' 修正的程式
try:
    n=float(input("請輸入正數 n："))
    n=int(n)
    for i in range(1,n+1):
        print(i,end=" ")
except Exception as e:
    print("發生錯誤的原因：" , e) 
'''