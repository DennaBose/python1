f1=open("in4.txt","r")
f2=open("out1.txt","w")
line1=f1.readline()
arr1=line1.split(",")
start=int(arr1[0])
end=int(arr1[1])
result=""
for j in range(start,end+1,1):
    for i in range(1,11,1):
        result=str(j)+"*"+str(i)+"="+str(j*i)
        f2.write(result+"\n")
        print(result)
    print()
    f2.write("\n")
f2.close()
