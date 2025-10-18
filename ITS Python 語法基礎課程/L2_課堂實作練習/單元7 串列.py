# 單元7 串列

#------------------------#
# 串列-產生、讀取串列, 串列的基本操作
fruit = ['橘子', '蘋果', '香蕉', '芭樂', '草莓'] #儲存字串
number = [1, 2, 3, 4, 5, 6, 7] #儲存數字
data = [10, "檸檬", True] #儲存不同資料型態

ans = [] #空串列

fruit = ['橘子', '蘋果', '香蕉', '芭樂', '草莓']

print(fruit[0]) #橘子
print(fruit[1]) #蘋果
print(fruit[4]) #草莓
print(fruit[5]) #讀取超出串列範圍會造成程式錯誤

# 修改串列
fruit[2] = '芭樂'
print(fruit) # ['橘子', '蘋果', '芭樂', '芭樂', '草莓']
print(fruit[2]) #芭樂

# 新增資料
fruit.append('鳳梨')
fruit.append('芒果')
print(fruit) #['橘子', '蘋果', '芭樂', '芭樂', '草莓', '鳳梨', '芒果']

# 移除資料
fruit = ['橘子', '蘋果', '芭樂', '芭樂', '草莓']
fruit.pop() #移除最後的元素 - 草莓
fruit.pop(1) #移除指定編號 1 的元素 - 蘋果
print(fruit)

# 插入資料
fruit = ['橘子', '蘋果', '芭樂', '芭樂', '草莓']
fruit.insert(3, '西瓜') #在編號3的位置插入一個的元素 - 西瓜
print(fruit)
#----------------#
# 串列-計算長度, 串接和複製, 範圍資料操作
fruit = ['橘子', '蘋果', '芭樂', '芭樂', '草莓']
print(len(fruit)) # 5

a = ['A', 'B', 'C']
b = ['C', 'D', 'E', 'F']
print(a + b) #['A', 'B', 'C', 'C', 'D', 'E', 'F']
print(a * 3) #['A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C']
print(a * 2 + b) #['A', 'B', 'C', 'A', 'B', 'C', 'C', 'D', 'E', 'F']

arr = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
print(arr[3:6]) #['D', 'E', 'F']
print(arr[2:8]) #['C', 'D', 'E', 'F', 'G', 'H']
print(arr[2:8:2]) #['C', 'E', 'G']
print(arr[1:8:3]) #['B', 'E', 'H']

arr = 'ABCDEFGHIJ'
print(arr[3:6]) #'DEF'
print(arr[2:8]) #'CDEFGH'
print(arr[2:8:2]) #'CEG'
print(arr[1:8:3]) #'BEH'
#----------------#
# 串列-list 與 join
fruit = 'apple'
arr = list(fruit)print(arr) #['a', 'p', 'p', 'l', 'e']
str1 = "".join(arr)
print(str1) # 'apple'














