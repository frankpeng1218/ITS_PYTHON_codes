month = int(input("請輸入月份："))
if (month>=1 and month<=3):
    print(month,"月是春天!")    
elif (month>=4 and month<=6):
    print(month,"月是夏天!")
elif (month>=7 and month<=9):
    print(month,"月是秋天!")
elif (month>=10 and month<=12):
    print(month,"月是冬天!")
else:
    print(month,"月份不在範圍內!")    