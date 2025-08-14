myList = [1,2,3,4,5]
f = open("/home/saaransh/Desktop/PYTHON/10_internal/chai.py")
print(iter(f) is f)
for lines in f:
    print(lines,end="")
I = iter(myList)
print(I is myList)
print(I.__next__())

print(I.__next__())
print(I.__next__())
print(I.__next__())
print(I.__next__())