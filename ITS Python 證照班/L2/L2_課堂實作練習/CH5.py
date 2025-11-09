# CH5 串列與元祖

# 重點複習 P5-2
#------------------------#
# 空串列：沒有任何元素的 list
a_empty_list = []
print("a_empty_list:", a_empty_list)

# 一維串列：可以放字串、數字、布林值等不同型態
a_list_one = ["Frank", 100, True, "Amy"]
print("a_list_one:", a_list_one)
print("印出Frank:", a_list_one[0])   # 取出第1個元素 (index=0)
print("印出100:", a_list_one[1])     # 取出第2個元素
print("印出True:", a_list_one[2])    # 取出第3個元素
print("印出Amy:", a_list_one[3])     # 取出第4個元素
print("index = -1:", a_list_one[-1]) # 從後面數第1個
print("index = -4:", a_list_one[-4]) # 從後面數第4個 (即第一個)

# 二維串列：串列中再放串列（像表格一樣）
a_list_two = [["A", "B"], ["C", "D"]]
print("印出A: ", a_list_two[0][0])
print("印出B: ", a_list_two[0][1])
print("印出C: ", a_list_two[1][0])
print("印出D: ", a_list_two[1][1])
#------------------------#


# 重點整理 P5-7 ~ 5-8
#------------------------#
# for 迴圈搭配 list 使用
train = ["Frank", "Winnie", "Bangbangbang"]
for t in train:
    print(t)
#------------------------#


# 重點整理 P5-9
#------------------------#
# len() 用來計算 list 的長度
train = ["Frank", "Winnie", "Bangbangbang"]
size = len(train)
print("train的長度為:", size)

# 逐一列出內容（方式1）
for t in train:
    print(t)

# 逐一列出內容（方式2）使用 index
for t in range(len(train)):  # range(3): 產生 0,1,2
    print(train[t])
#------------------------#


# 重點整理 P5-12
#------------------------#
# append()：在最後加入新元素
# insert()：在指定位置插入新元素
big_train = ['Frank', 'Bruce', 'Roy', 'BenBenBen', 'Leo']
print("原始狀態:", big_train)
big_train.append('Winnie')
print("加入Winnie後: ", big_train)
big_train.insert(1, "大媽")
print("大媽插在index=1的地方後:", big_train)
#------------------------#


# 重點整理 P5-15
#------------------------#
# remove()：移除指定元素
# pop()：移除並回傳最後一個或指定位置的元素
# del：刪除指定索引或範圍的元素

big_train.remove("大媽")
print("刪掉大媽後:", big_train)

pop_item_0 = big_train.pop()
print("pop()之後:", big_train)
print("被pop()的元素是:", pop_item_0)

pop_item_1 = big_train.pop(1)
print("pop(1)之後:", big_train)
print("被pop(1)的元素是:", pop_item_1)

list_a = [1, 3, 5, 7, 9]
print("原本的list_a:", list_a)
del list_a[2]  # 刪除 index=2 的元素
print("del list_a[2]後的list_a:", list_a)

list_b = [2, 4, 6, 8, 10]
print("原本的list_b:", list_b)
del list_b[1:4:2]  # 刪除索引1到3之間、間隔2的元素 (即 index 1 和 3)
print("del list_b[1:4:2]後的list_b:", list_b)
#------------------------#


# 重點整理 P5-19 ~ 5-21
#------------------------#
# sort()：由小到大排序
# reverse()：反轉順序

list_c = [2, 4, 1, 100, 3, 9, 8]
print("原本的list_c:", list_c)
list_c.sort()
print("排序後的list_c:", list_c)

list_d = [1, 2, 3, 4, 5, 6, 7]
print("原本的list_d:", list_d)
list_d.reverse()
print("反轉後的list_d:", list_d)

# 由大到小排序 - 方法1（使用 sort(reverse=True)）
list_e = [2, 4, 1, 100, 3, 9, 8]
print("原本的list_e:", list_e)
list_e.sort(reverse=True)
print("由大到小排序後的list_e:", list_e)

# 由大到小排序 - 方法2（使用 sorted() 回傳新串列）
list_f = [2, 4, 1, 100, 3, 9, 8]
print("原本的list_f:", list_f)
list_new_f = sorted(list_f, reverse=True)
print("排序後的新串列 list_new_f:", list_new_f)
#------------------------#


# 重點整理 P5-23
#------------------------#
# 串列切片 (slice)：a[start:end:step]
a = [1, 3, 5, 7, 9]
b = a[1:4:2]  # 取 index 1~3，每隔2個取一次 → [3, 7]
print("b:", b)
c = a[0:3]    # 取 index 0~2 → [1, 3, 5]
print("c:", c)
d = a[:3]     # 省略開頭，從0開始取 → [1, 3, 5]
print("d:", d)
e = a[1:]     # 省略結尾，從index=1取到最後 → [3, 5, 7, 9]
print("e:", e)
f = a[::2]    # 從頭到尾每隔2個取一次 → [1, 5, 9]
print("f:", f)
#------------------------#


# 重點整理 P5-24
#------------------------#
# 元祖 (tuple)：內容不可變動，用小括號 ()
a_tuple = (1, 3, 5)
print("取出元祖中第3個元素:", a_tuple[2])
