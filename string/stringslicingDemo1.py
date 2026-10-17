data = "ahmedabad"
print(data)
print(data[0])
print(data[-1])
print(data[0:4:1]) #satrts with 0 end to 4 incemrnt 1
print(data[:5:1])
print(data[::1]) #starts with 0 end to len and incrmeent by 1
print(data[::2])
print(data[0::])
print(data[1::])

print(data[0:-1])
print(data[0:-2])

print(data[::-1])

name = "ajay"
if name == name[::-1]:
    print("palindrome")
else:
    print("not plaindrome")    