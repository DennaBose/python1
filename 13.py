import os
from datetime import datetime as dt
#8_20210828_110503.txt
today=dt.now()
dir1="/TABLES/"
start=10
end=20
result1=""
for j in range(start,end+1,1):
    part1=str(j)
    part2=today.strftime("_%Y%m%d_%H%M%S")
    part3=".txt"
    fname1=part1+part2+part3
    #fname2=os.path.join(dir1,fname1)
    f1=open(fname1,"w")
    for i in range(1,11,1):
        result1=str(j)+"*"+str(i)+"="+str(j*i)
        f1.write(result1+"\n")
        print(result1)
    print()
    f1.close()


