filename=input("請輸入檔案名稱：")

try:
    f=open(filename,'r')
    for line in f:
        print(line,end="")
    f.close()
except:
    print("檔案不存在或無法開啟檔案!")