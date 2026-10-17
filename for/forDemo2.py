#fibonaci series
# 0  1  1  2  3  5 8..
a = 0
b = 1
print(a,b,end=" ") # 0 1
for i in range(1,10):
    sum = a+b #sum =2
    print(sum,end=" ")
    a = b #a =1
    b = sum #b =2
    
    
    