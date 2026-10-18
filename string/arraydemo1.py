from array import array
marks = array('i',[10,20,30,10,10,40,50])
print(marks)
print(marks[0])
print(marks.typecode)
print(marks.itemsize)

#append

marks.append(21)
print(marks)
marks.extend([40,50,55])
print(marks)

marks.insert(2,99)
print(marks)

#remove
marks.remove(40)
print(marks)

#marks.pop(4)
marks.pop()#last index remove
print(marks)

#check index..

ind = marks.index(99)
print("index",ind)

print(marks.count(10))

#reverse

marks.reverse()
print(marks)


#slicing

print(marks[0])
print(marks[len(marks)-1])
print(marks[-1])
print(marks[-2])

print(marks[0::2])
print(marks[0:3])

marks.clear()
print(marks)