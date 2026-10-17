email = "  samir @ gmail.com    "
print(email)

email = email.strip()
print(email)

newemail=""
#manual loop

for i in email:
    if " " not in i:
        newemail+=i

print(newemail)        
        
