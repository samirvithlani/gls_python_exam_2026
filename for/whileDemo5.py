#153
#1^3 +  .. = 153

no = 54748
tempno = no
temp2=no
sum=0
count=0

while temp2!=0:
    count+=1
    temp2= temp2//10
    

while no!=0:
    rem = no %10
    sum = sum + (rem**count)
    no = no//10

print(sum)    
if sum==tempno:
    print("\n armstrong...")
else:
    print("\n no")    
    