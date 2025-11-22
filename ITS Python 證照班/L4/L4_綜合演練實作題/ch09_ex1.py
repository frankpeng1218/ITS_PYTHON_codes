file = "in_a.txt"
with open(file,'r') as f:
    content=f.readlines()    
   
for row in content:
    n = len(row)
    print("字元數=%2s : %s" %(n,row)) 