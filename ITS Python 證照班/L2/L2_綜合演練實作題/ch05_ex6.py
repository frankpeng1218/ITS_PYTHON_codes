animals = "鼠牛虎免龍蛇馬羊猴雞狗豬"
year = int(input("請輸入你的出生西元年："))
print("西元{}年出生屬{}".format(year, animals[(year-2020) % 12]))