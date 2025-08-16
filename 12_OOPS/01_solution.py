class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    def fullName(self):
        print(f"{self.brand} {self.model}")

skoda =  Car("Toyota","Fortuner")
print(skoda.brand)
print(skoda.model)

Endavor = Car("Ford","Endavour")
print(Endavor.fullName())
