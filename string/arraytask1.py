# import numpy as np

# seating = np.array([[101,102,103],[104,105,106],[107,108,109]])
# row = int(input("enter row[1-3] : "))
# col = int(input("enter row[1-3] : "))


# roll_no = seating[row-1,col-1]
# print(roll_no)

seating = [[101,102,103],[104,105,106],[107,108,109]]
row = int(input("enter row[1-3] : "))
col = int(input("enter row[1-3] : "))

roll_no = seating[row-1][col-1]
print(roll_no)
