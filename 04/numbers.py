import math
import random
x = 10
y = 20
z = 30

print(x,y,z)
print(x < y and y < z)

print(math.floor(3.7))

print(math.ceil(3.7))

# print(math.radians(100))

print(99999999999 * 2.1)

print(0b10000)

print(math.floor(random.random() * 10))

list1 = ["r","p","s"]
print(random.choice(list1))

def random_number():
    user_input = input("Enter r, p or s: ")
    computer_choice = random.choice(list1)
    if user_input == computer_choice:
        print("It's a tie")
    match user_input:
        case "r":
            if computer_choice == "p":
                print("You lose")
            else:
                print("You win")
        case "p":
            if computer_choice == "s":
                print("You lose")
            else:
                print("You win")
        case "s":
            if computer_choice == "r":
                print("You lose")
            else:
                print("You win")    

# random_number()


setOne = {1,2,3}
setTwo = {3,4,5}

print(setOne & setTwo)
print(setOne | setTwo)
