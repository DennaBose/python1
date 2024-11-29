def calc(num1,num2):
    
    
    sum1=num1+num2
    sub1=num1-num2
    mul1=num1*num2
    div1=num1/num2
    div2=num1//num2
    mod1=num1%num2
    exp1=num1**num2
    print (sum1,sub1,mul1,div1,div2,mod1,exp1)
f1=open("in1.txt","r")
n1=int(f1.readline())
n2=int(f1.readline())
print(n1)
print(n2)
calc(n1,n2)
