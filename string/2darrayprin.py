users = [["raj","ram"],["parth","priya"],["neha","naman"]]
print(users)

#range loop

# for i in range(0,len(users)):
#     #print(users[i]) #arrays
#     for j in range(0,len(users[i])):
#         print(users[i][j],end=" ")
#     print()    
    
#for each loop

# for i in users:
#     #print(i)
#     for j in i:
#         print(j,end=" ")
#     print()    


marks = [[20,21],[23,24],[19,21],[22,25]]

# for i in marks:
#     #print(i)
#     for j in i:
#         print(j,end=" ")
#     print()    

# sum=0
# for i in marks:
#     #print(i)
#     for j in i:
#         print(j,end=" ")
#         sum+=j
#     print()   

# print("total sum =",sum)     



sum=0
rowsum =0
for i in marks:
    #print(i)    
    for j in i:
        rowsum+=j
        print(j,end=" ")
        sum+=j     
    print(" = ",rowsum,end=" ")    
    rowsum=0
    print()   

print("total sum =",sum)     
