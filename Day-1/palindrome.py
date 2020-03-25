l=[]
a=str(input("Enter an word"))
b=a.split()
for word in b:
    if word[::-1]==word:
        l.append(word)
        print("The number of palindromes is : " ,len(l))
    
    

     
        
        

    
