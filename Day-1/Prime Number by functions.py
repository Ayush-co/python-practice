def my_func(a):
    for i in range(2,a):
        if a%i==0:
            print("It is not a prime number")
            break
    
    else:
            print("It is a prime number")
my_func(2)
my_func(8)
my_func(27)
my_func(29)
