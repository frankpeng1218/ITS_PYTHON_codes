monthname = {1:'JAN', 2:'FEB', 3:'MAR', 4:'APR', 5:'MAY', 6:'JUN', 7:'JUL', 8:'AUG', 9:'SEP', 10:'OCT', 11:'NOV', 12:'DEC'}
m = int(input("【查詢月份簡寫】\n請輸入要查詢的月份數字："))
print("{}月份的英文簡寫為 {}：".format(m, monthname[m]))