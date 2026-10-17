# and or not

#cond1 and cond2
# T  --> T  ---->T
# T --->F --->F
# f ----------->F

#cond1 or cond2
#T -------->T
#F ---->T ---->T
#F ---->F---->F

aadhar = True
Dl = False

# if aadhar==True or Dl == True:
#     print("eligible...")
# else:
#     print("not eligible")    

if aadhar or Dl:
    print("eligible...")
else:
    print("not eligible")
