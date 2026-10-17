#rev.


no = 121
copyno =no
rev =0

while no!=0:
    rem = no % 10 #3 2 1
    rev = (rev*10)+rem #(0)+3 =321
    no = no //10 # //12 // 1

print("rev",rev)    
    
    
if rev==copyno:
    print("no is palindrome")
else:
    print("no is not palindrome")    
    