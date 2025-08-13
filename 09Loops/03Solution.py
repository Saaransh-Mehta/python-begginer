num = int(input("Enter the number youwant a table for : "))

for i in range(11):
    if(i == 5):
        continue
    print(num * i)