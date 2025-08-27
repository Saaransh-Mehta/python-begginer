class Student:
    def __init__(self):
        self.name = ""
        self.age=0
        self.rollNo = 0
    def options(self):
        print('''
            ----------------
              Following options to perform some operations

              1. Press 1 For Student Registration
              2. Press 2 For Student Data Deletion
              3. Press 3 For Print Details
        ''')
        user_input = int(input("Enter the value"))
        if user_input == 1:
            self.register()
        elif user_input == 2:
            self.delete()
    
    def register(self):
        self.name = input("Enter the name : ")
        self.age = int(input("Enter the age : "))
        self.rollNo = int(input("Enter the roll number: "))

    def print(self):
        print(f"Student Name : {self.name} , Age : {self.age} , Roll Number : {self.rollNo}")
    
    def delete_record(self):
        del self.name
        del self.age
        del self.rollNo




