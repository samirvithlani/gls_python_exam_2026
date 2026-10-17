#string concat:

fname = "raj"
lname = "shah"

fullname = fname + " " +lname
print(fullname)

#revrse and concat:

name = "naman"
revname =""

#4 -1 -1
for i in range(len(name)-1,-1,-1):
    #print(name[i])
    revname+=name[i]

print(revname)    

if name==revname:
    print("name is palindrome ")
else:
    print("name is not plaindrome")    
    
