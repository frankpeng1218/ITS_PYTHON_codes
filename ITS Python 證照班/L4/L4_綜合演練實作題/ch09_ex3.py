fout=open('myFile.txt','w')

word=""
while True:
    str=input("請輸入文字[Enter]結束輸入並存檔：")
    if (str==""):
        break   
    word += (str + "\n")
    
print(word)       # 顯示輸入文字
fout.write(word)  # 寫入檔案
fout.close()