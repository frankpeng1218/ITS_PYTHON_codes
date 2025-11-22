file = "file3.txt"
with open(file,'r') as f:
    content=f.readlines()
    
i=1    
for row in content:
    print("%2s : %s" %(i,row)) 
    i+=1 