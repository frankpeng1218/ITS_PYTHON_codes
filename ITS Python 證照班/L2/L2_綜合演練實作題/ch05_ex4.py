numbers = [1, 2, 3, 4, 2, 7, 3, 2, 3]
numbers2 = []
for number in numbers:
    n = numbers2.count(number)  #計算出現次數
    if (n == 0): #將不重複數字放入 numbers2 串列
        numbers2.append(number)
print(numbers2)