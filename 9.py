start=int(input("Enter a start number "))
end=int(input("Enter a end number "))
for j in range(start,end+1,1):
    for i in range(1,11,1):
        print(j,"*",i,"=",j*i)
    print()    
