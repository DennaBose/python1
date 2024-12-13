months=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
days=[31,28,31,30,31,30,31,31,30,31,30,31]
dayOfWeek=["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
count=0
for j in range(0,12,1):
    for i in range(1,days[j]+1,1):
        print(dayOfWeek[(2+count)%7]+", "+months[j]+" "+str(i))
        count=count+1
    print()


