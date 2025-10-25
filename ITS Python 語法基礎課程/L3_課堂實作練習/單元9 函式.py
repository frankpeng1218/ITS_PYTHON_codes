# 單元9 函式

#------------------------#
# 函式-設計函式
def juicer(fruit):
    drink = fruit + '汁'
    return drink
a = juicer('香蕉')
b = juicer('榴蓮')
print(a) #印出香蕉汁
print(b) #印出榴蓮汁

#只有輸出的函式
def test_1():
    return '你好'
r = test_1()
print(r) #印出「你好」

#只有輸入的函式
def test_2(count):
    for i in range(count):
        print('嗨')
test_2(10) #印出 10 次「嗨」

#沒有輸出與輸出的函式
def test_3():
    print('嗨嗨')
    test_3() #印出嗨嗨
#----------------#
# 函式-預設參數
def sum(a, b):
    return a + b
sum(10, 20) #會得到數值 30
sum(10) #執行時產生錯誤

def sum(a, b=10):
    return a + b
sum(10, 20) #會得到數值 30
sum(10) #會得到數值 20
#----------------#
# 函式-內建函式
int('10') #整數 10
float('10.5') #將字串轉成浮點數 10.5
str(123) #將數值轉成字串 '123'
len([10, 20, 30]) #計算串列的長度取得數值 3
len('今天天氣真好！') #計算字串長度取得數值 7
#----------------#












