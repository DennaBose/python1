start=3
end=5
result1=""
for j in range(start,end+1,1):
    part1=str(j)
    part2=".txt"
    fname1=part1+part2
    f1=open(fname1,"w")
    for i in range(1,11,1):
        result1=str(j)+"*"+str(i)+"="+str(j*i)
        f1.write(result1+"\n")
        print(result1)
    print()
    f1.close()


