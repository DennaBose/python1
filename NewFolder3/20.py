prison=["O"]*100
len1=len(prison)
for i in range(1,len1,1):    
    for j in range(i,len1,i+1):
        if prison[j]=="C":
            prison[j]="O"
        else:
            prison[j]="C"
for k in range(0,len1,1):
    if prison[k]=="O":
        print(k+1)
