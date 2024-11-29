def calc(num1,num2):
    
    
    sum1=num1+num2
    sub1=num1-num2
    mul1=num1*num2
    div1=num1/num2
    div2=num1//num2
    mod1=num1%num2
    exp1=num1**num2
    result1=str(sum1)+" "+str(sub1)+" "+str(mul1)+" "+str(div1)+" "+str(div2)+" "+str(mod1)+" "+str(exp1)
    return result1
f1=open("in2.txt","r")
f2=open("out1.txt","w")
line1=f1.readline()
arr1=line1.split(",")
n1=int(arr1[0])
n2=int(arr1[1])
output1=calc(n1,n2)
f2.write(output1)
print(output1)
f2.close()

