year = int(input("請輸入一個西元年："))
if year % 100 == 0:
    if year % 400 == 0:
        print("西元 {} 年是閏年".format(year))
    else:
        print("西元 {} 年不是閏年".format(year))
else:
    if year % 4 == 0:
        print("西元 {} 年是閏年".format(year))
    else:
        print("西元 {} 年不是閏年".format(year))