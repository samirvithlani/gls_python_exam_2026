#string is immutable..
#no modificaiton is allow
#string stores data in index
#in python string supprorts neg index

name = "royal"
#r=0
#a=1 ..
print(name)
print("0",name[0]) #0
print("-1",name[-1]) #-1 -- last char
print("-2",name[-2]) #-1 -- last char

#name[0] = "R" #cahnge index value -->0 -->r -->R  TypeError: 'str' object does not support item assignment
print(name) #Royal

