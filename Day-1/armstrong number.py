a=int(input("Enter an number"))
sum=0
i=a
while a>0:
    digit=a%10
    sum=sum+digit**3
    a=a//10
    if i==sum:
        print("It is an armstrong number")
        break
else:
    print("it is not an armstrong number")
    
