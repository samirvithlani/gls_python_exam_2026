for i in range(1,6):
    for j in range(1,6):
        print("*",end=" ")
    print()    


for i in range(1,6):
    for j in range(1,i+1):
        print("*",end=" ")    
    print()    
    

for i in range(1,6):
    for j in range(1,i+1):
        print(i,end=" ")    
    print()    

for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")    
    print()            

k=0

for i in range(1,6):
    for j in range(1,i+1):
        k+=1
        print(k,end=" ")    
    print()     

for i in range(1,6):
    for j in range(1,i+1):
        print(chr(i+64),end=" ")    
    print()            
        
for i in range(1,6):
    for j in range(1,i+1):
        print(chr(j+64),end=" ")    
    print()              


#pyramid

for i in range(1,6):
    print(" "*(5-i),end="")
    print("*"*(2*i-1)) 

for i in range(1,6):
    print(" "*(5-i)+"*"*i)    