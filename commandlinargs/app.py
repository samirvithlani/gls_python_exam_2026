import sys
print("commandline argument",sys.argv)
name = sys.argv[0]
print(name)

if len(sys.argv) != 3:
    print("min 3 command line args are required!!")
    sys.exit(1)

no1 = int(sys.argv[1])
no2 = int(sys.argv[2])

print(no1+no2)


