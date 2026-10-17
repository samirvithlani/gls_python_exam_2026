#check no is even or odd using & bitwise op

no =14
print(f"bin of no = {bin(no)}")
print(f"bin of 1 = {bin(1)}")
print(f"{no|1}")

print(f"{no|0}")

# 13 | 1 == 13
# 30 | 0 = 30
# 23 | 1 = 23
if(no|0) == no:
    print("no is even")
else:
    print("no is odd")    