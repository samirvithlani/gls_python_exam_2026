import sys

if(len(sys.argv))!=4:
    print("min 4 arg are required !")
    sys.exit(1)

a= float(sys.argv[1])    
op = sys.argv[2]
b = float(sys.argv[3])    

if op =="+":
    print(a+b)
elif op=="-":
    print(a-b)
elif op=="*":
    print(a*b)    
