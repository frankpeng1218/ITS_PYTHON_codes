mh = int(input("請問你的身高是幾公分？"))
ih = mh / 2.54
i1 = ih // 12  # 英呎
i2 = ih % 12   # 英吋
print("身高 %d 公分等於 %d 呎 %.f 吋" % (mh, i1, i2))