def even_nums_till_limit():
    num = int(input("Enter the number : "))
    for i in range(num + 1):
        if(i % 2 == 0):
            print(i)
        else:
            continue

even_nums_till_limit()