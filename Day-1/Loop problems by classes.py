class myclass1:
    def __init__(self,a):
        self.a=a

p1=myclass1(8)
if (p1.a)%2==0:
    print("It is an even number")
else:
    print("It is an Odd number")


class myclass2:
    def __init__(self,b):
        self.b=b

p2=myclass2(3)
for i in range(2,p2.b):
    if (p2.b)%i==0:
        print("It is not an prime number")
        break
else:
    print("It is an prime number")


class myclass3:
    def __init__(self,c):
        self.c=c

p3=myclass3("mom")
if p3.c[::-1]==p3.c:
    print("It is an palindrome")
else:
    print("It is not an palindrome")
    
    
    
        
