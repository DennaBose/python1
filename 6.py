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

f2=open("out1.txt","w")
output1=calc(10,5)
f2.write(output1)
f2.write("\n")
print(output1)
output1=calc(8,2)
f2.write(output1)
print(output1)
output1=calc(15,7)
f2.write(output1)
print(output1)
f2.close()

