def age_categorization():
    age = int(input("Enter your age"))
    Child = []
    Teenager = []
    Adult = []
    Senior = []

    if(age < 13):
        Child.append(age)
    elif(age > 13 and age <=19):
        Teenager.append(age)
    elif(age > 19 and age <= 59):
        Adult.append(age)
    elif(age > 59 ):
        Senior.append(age)
    print(Child)
    print(Teenager)
    print(Adult)
    print(Senior)

age_categorization()

