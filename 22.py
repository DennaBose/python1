months=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
days=[31,28,31,30,31,30,31,31,30,31,30,31]

for j in range(0,12,1):
    for i in range(1,days[j]+1,1):
        print(months[j]+" "+str(i))
    print()


