name = input("enter name :")
print(name)

#how to find string len

l = len(name)
print("len of string",l)



# for i in range(0,5): #0 1 2 3 4
#     print(name[i])

# for i in range(0,l):
#     print(name[i],end=" ")

# for i in range(0,len(name)):
#     print(name[i],end=" ")

#for each loop advance for loop

#by default it starst from 0 and end to len of string -1
for i in name:
    print(i,end=" ")