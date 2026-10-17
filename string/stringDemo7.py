#builtin functions

name = "raj"
#name.upper() #string is immutable
name = name.upper() #new ref
print(name)
name = name.lower()
print(name)

data = "hi this is ahmeadbad"
#data = data.title()
data = data.capitalize()
print(data)
data1 = "Hi THiS iS AhMEDabad"
data1 = data1.swapcase()
print(data1)

email = "  samir@gmail.com   " #15
print(email)
print(len(email))

#remove unwanted white space..

# email = email.lstrip()
# print(email)
# print(len(email))

# email = email.rstrip()
# print(email)
# print(len(email))

email = email.strip()
print(email)
print(len(email))