prison=['C','C','C','C','C','C','C','C','C','C']
len1=len(prison)
for i in range(0,len1,1):
    prison[i]="O"
print(prison)
for i in range(1,len1,2):
    prison[i]="C"
print(prison)

for i in range(j,len1,j+1):
    if prison[i]=="C":
        prison[i]="O"
    else:
        prison[i]="C"
print(prison)
for i in range(3,len1,4):
    if prison[i]=="C":
        prison[i]="O"
    else:
        prison[i]="C"
print(prison)
for i in range(4,len1,5):
    if prison[i]=="C":
        prison[i]="O"
    else:
        prison[i]="C"
print(prison)
