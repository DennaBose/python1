for j in range(0,4,1):
    for i in range(0,12,1):
        angle1=90-30*j+i*30-i*2.5
        print(angle1%360)
    print()
