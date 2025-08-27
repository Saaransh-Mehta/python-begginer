x = int(input("Enter the value for x :"))
y = int(input("Enter the value for y :"))
z = int(input("Enter the value for z : "))

if x > y and x > z:
    print("X is greatest and the value of x is :", x)
elif y > z and y > x:
    print("Y is greatest and the value for y is : ", y)
else:
    print("Z is greater than all",z)
print(max(x,y,z))
    
list1 = list((x,y,z))
list1.sort()
print(list1)
print(list1[len(list1) - 1])

