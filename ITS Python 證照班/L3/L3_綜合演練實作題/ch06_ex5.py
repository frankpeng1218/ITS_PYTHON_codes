rate = {'USD':28.02, 'JPY':0.2513, 'CNY':4.24}
TWD = float(input("請輸入台幣："))
print("台幣{:.2f}元等於美金{:.2f}元, 日幣{:.2f}元, 人民幣{:.2f}元".format(TWD, TWD/rate['USD'], TWD/rate['JPY'], TWD/rate['CNY']))