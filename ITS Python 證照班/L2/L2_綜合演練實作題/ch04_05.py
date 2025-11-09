p=1
counter=0
n = int(input("請輸入正整數："))
print(n,"的因數有",end=" ")
while (p<=n):
    if (n%p==0):
        print(p,end=" ")
        counter+=1
    p+=1

print()    
if (counter==2):    
    print(n,"是質數")
else:
    print(n,"不是質數")