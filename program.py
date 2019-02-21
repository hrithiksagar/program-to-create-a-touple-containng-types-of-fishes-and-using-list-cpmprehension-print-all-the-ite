x=[]
y=int(input("enter size of touple: "))
for i in range(y) :
    l=input("Enter fishes name")
    x.append(l)
z=[i for i in x if i!="octopus"]
z=tuple(z)
print(z) 
