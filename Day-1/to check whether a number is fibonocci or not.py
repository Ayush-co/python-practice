def myperfectsquare(x):
    s=int(x**(1/2))
    return s*s==x
def myfibonoocci(n):
    return myperfectsquare(5*n*n+4) or myperfectsquare(5*n*n-4)
for i in range(1,20):
    if(myfibonoocci(i)==True):
        print("It is a fibonocci number: ", i)
    else:
        print("It is not an fibonocci number: ", i)
    
