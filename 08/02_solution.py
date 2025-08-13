age = int(input("Enter your age"))
day = input("What day is it : ")
price = 0
def movie_ticket():
    if(age < 18):
        if(day=="Wednesday"):
            price = "$6"
        else:
            price = "$8"
    elif(age >= 18):
        if(day=="Wednesday"):
            price = "$10"
        else:
            price = "$12"

    print(price)

movie_ticket()