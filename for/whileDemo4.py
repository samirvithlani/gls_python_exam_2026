#153
#1^3 +  .. = 153

no = 153
tempno = no
sum=0
while no!=0:
    rem = no %10
    sum = sum + (rem**3)
    no = no//10

print(sum)    
if sum==tempno:
    print("\n armstrong...")
else:
    print("\n no")    
    