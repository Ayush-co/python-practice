a=int(input("Enter the number"))
if a<0:
    print("The factorial of the number does not exist")
elif a==0:
    print("The factorial of the number is one ")
else:
    i=1
    for i in range(1,a):
        a=a*i
print(a)



