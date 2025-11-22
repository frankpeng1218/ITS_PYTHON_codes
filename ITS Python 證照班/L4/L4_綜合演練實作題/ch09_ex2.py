file = "in_a.txt"
with open(file,'r') as f:
    content=f.read()

n=0
for ch in content:
    if (ch=="A" or ch=="a"):
        n+=1
print("共有",n,"個 A 或 a 字元") 