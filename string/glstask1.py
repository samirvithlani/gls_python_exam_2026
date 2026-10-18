#revers sring using slicing:

name  ="raj"
revname  = name[::-1]
print(revname)

print(name[0])
print(name[len(name)-1])

count=0
for i in name:
    if "a" in i:
        count+=1

print(count)        

data = "I love Python"

if "Python" in data:
    print("yes")
else:
    print("no")    

data = data.replace("Python","Java")    

print(data)

#split
data = "Python is Easy"

x = data.split(" ")
print(x)

data1 = " ".join(["I","Love","Python"])
print(data1)