# 單元5 條件判斷

#------------------------#
# 條件判斷-and, or, not, if 條件判斷
a = True
b = False
c = a or b
d = a and c
e = not c
print(a, b, c, d, e)

score = int(input("請輸入你的成績:"))
# 記得要縮排的觀念
if score >= 60:
    print('及格')
#----------------#
# 條件判斷-if - else 條件判斷, if - elif - else 條件判斷
score = int(input("請輸入你的成績:"))
if score >= 60:
    print('及格')
if score < 60:
    print('不及格')
if score >= 60:
    print('及格')
else:
    print('不及格')


score = int(input('成績: '))
if score >= 90:
    print('A 級')
else:
    if score >= 80:
        print('B 級')
    else:
        if score >= 70:
            print('C 級')
        else:
            if score >= 60:
                print('D 級')
            else:
                print('E 級')

score = int(input('成績: '))
if score >= 90:
    print('A 級')
elif score >= 80:
    print('B 級')
elif score >= 70:
    print('C 級')
elif score >= 60:
    print('D 級')
else:
    print('E 級')










