with open("intro.txt") as a:
    data=a.read()
with open("Data.txt") as a:
    data1=a.read()
data+="\n"
data+=data1
with open("Data-2.txt","w") as a:
    a.write(data)



        
        


