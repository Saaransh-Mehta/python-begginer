class ATM:
    def __init__(self):
        self.pin = ""
        self.balance = 0

    def main(self):
        user_input = int(input('''
        HI There welcome to ATM
        1. Setup pin
        2. Update balance
        '''))

        if user_input == 1:
            pin_input = input("What is your new pin: ")
            self.pin = pin_input
        elif user_input == 2:
            self.balance = int(input("Enter the money: "))

    def printStatus(self):
        user_input = int(input('''
        Press 1 for balance
        '''))
        if user_input == 1:
            print(self.balance)


pnb = ATM()
pnb.main()
pnb.printStatus()
