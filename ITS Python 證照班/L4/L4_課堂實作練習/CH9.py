# CH9 檔案與例外處理
# 重點整理 P9-2
# ------------------------#
# 傳統 Windows（繁中）預設 cp950, 其餘都是UTF-8
# 開啟檔案的語法：
# open( filename [, mode] [, encode] )
# filename 是必填參數, 其他則為選擇性或不填使用預設值
# 一定要有test.txt這個檔案存在
# 以讀取模式 r 開啟檔案
f = open("file1.txt", "r")  # 開啟檔案
content = f.read()         # 讀取內容
print(content)
f.close()                  # 關閉檔案
#------------------------#

# 重點整理 P9-2, P9-4
#------------------------#
# 開啟檔案的模式, 使用 with … as 語法
with open("file1.txt", "r", encoding="utf-8") as f:
    print(f.read())
    
# r：讀取模式
with open("file1.txt", "r") as f:   # 以讀取模式 r 開啟 file1.txt
    print(f.read())                # 讀取並印出檔案內容

# w：寫入模式，若檔案已存在，內容將會被覆蓋
with open("file1.txt", "w") as f:   # 以寫入模式 w 開啟（會清空原內容）
    f.write("Hello\n")             # 寫入新的內容

# a：附加模式，若檔案已存在，新增的內容會被附加於尾端
with open("file1.txt", "a") as f:   # 以附加模式 a 開啟（寫在最後）
    f.write("Add more text\n")     # 在檔案尾端新增內容

# b：檔案為二進位模式
with open("photo.jpg", "rb") as f: # 以二進位模式 rb 開啟圖片
    data = f.read()                # 讀取圖片的二進位資料

# +：打開一個檔案進行更新（可讀可寫）
#   （此例使用 r+ 示範 read + write）
with open("file1.txt", "r+") as f:  # 以 r+ 模式開啟，可讀可寫
    pass                            # 示範模式用，這行不做任何事

# r+：打開一個檔案用於讀寫，讀寫的位置在檔案的起頭
with open("file1.txt", "r+") as f:  # 以 r+ 開啟，不會清除內容
    content = f.read()             # 讀取整個檔案內容
    f.seek(0)                      # 游標移回檔案開頭
    f.write("EDIT")                # 從開頭開始覆蓋文字

# w+：打開一個檔案用於讀寫，會清空舊內容，若不存在則建立新檔
with open("file1.txt", "w+") as f:  # 以 w+ 開啟，先清空檔案
    f.write("New content\n")       # 寫入新內容
    f.seek(0)                      # 游標移回開頭
    print(f.read())                # 讀取並印出剛寫入的內容
#------------------------#


# 重點整理 P9-5, P9-5 ~ 9-8
#------------------------#
# 檔案處理

# close()：關閉檔案並將資料寫入到檔案中
f = open("file2.txt", "r")          # 以讀取模式開啟
print(f.read())                     # 讀取全部內容
f.close()                           # 關閉檔案

# read()：讀取指定長度；若未指定則讀取全部內容
with open("file2.txt", "r") as f:
    print(f.read(10))               # 讀取前 10 個字元
    # print(f.read())               # 若不指定長度 → 讀全部

# readline()：讀取一整行（包含 '\n'）
with open("file2.txt", "r") as f:
    for line in f:                  # 使用 for 逐行讀取
        print(line, end="")         # end="" 避免多印一個換行
    print()                         # 最後補一個換行（排版）

# readlines()：一次讀取所有行，回傳「行的列表」
with open("file2.txt", "r") as f:
    lines = f.readlines()           # 每一行變成一個元素
    print(lines)                    # 印出列表內容

# seek()：將讀取指標移到指定位置
with open("file2.txt", "r") as f:
    f.seek(0)                       # 指標移到檔案開頭
    print(f.readline())             # 讀取第一行

    f.seek(7)                       # 指標移到檔案第 7 個字元位置
    print(f.read(12))               # 從該位置開始讀 12 個字元

# write()：將資料寫入檔案（可連續操作）
with open("file2.txt", "w") as f:
    f.write("AAA\n")                # 第一行
    f.write("BBB\n")                # 第二行
    f.write("CCC\n")                # 第三行
#------------------------#

# 重點整理 P9-9
#------------------------#
# 檔案和目錄管理
import os
import os.path

# os.path.isfile()：判斷是否為檔案
print(os.path.isfile("file2.txt"))   # 若 file2.txt 存在且是檔案 → True

# os.path.isdir()：判斷是否為資料夾
print(os.path.isdir("myfolder"))     # 若 myfolder 是資料夾 → True

# os.path.exists()：判斷檔案或資料夾是否存在
print(os.path.exists("file2.txt"))   # 判斷 file2.txt 是否存在
print(os.path.exists("myfolder"))    # 判斷 myfolder 是否存在

# os.remove()：刪除檔案
# os.remove("file2.txt")             # 刪除 file2.txt（使用前請確定檔案存在）

# os.mkdir()：建立資料夾
# os.mkdir("new_dir")                 # 建立 new_dir 資料夾

# os.rmdir()：刪除空資料夾（資料夾裡不能有任何檔案）
# os.rmdir("new_dir")                 # 刪除 new_dir 資料夾（需為空資料夾）

# os.getcwd()：取得目前程式所在位置
print(os.getcwd())                  # 印出目前工作目錄
#------------------------#

# 重點整理 P9-11, P9-13 ~ P9-14
#------------------------#
# 例外處理
# try-except-except：分別處理不同錯誤
try:
    x = int("abc")            # 會產生 ValueError
except ValueError:
    print("發生數值轉換錯誤！")
except Exception:
    print("發生其他錯誤！")

# try-except-else-finally：完整結構
try:
    x = 10 / 2                # 正常運作，沒錯誤
except ZeroDivisionError:
    print("除以零錯誤")
else:
    print("程式沒有錯誤，因此執行 else 區塊")
finally:
    print("不論是否錯誤，都會執行 finally")

# try-finally：不處理錯誤，但 finally 保證執行
try:
    f = open("file2.txt", "r")   # 嘗試開啟檔案
    print(f.read())
finally:
    print("結束時一定會執行（例如關閉檔案）")











