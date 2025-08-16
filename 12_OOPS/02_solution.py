class Cars:
    def __init__(self,brand,model):
        self.__brand = brand
        self.model = model
    def fullName(self):
        return f"{self.__brand} {self.model}"
    @staticmethod
    def general_desription():
        return "Chasis Number is undefined"
    @property
    def get_brand(self):
        return self.__brand


class ElectricCar(Cars):
    def __init__(self,__brand,model,battery_size):
        super().__init__(__brand,model)
        self.batterySize = battery_size
    
    def fullStats(self):
        return f"{self.model} by {self.brand} have battery size of {self.batterySize}"


# ev_car = ElectricCar("Tesla","S Model","100KWH")
# print(ev_car.__brand)
# print(ev_car.fullName())
# print(ev_car.fullStats())
new_car = Cars("Toyota","Fortuner")
print(Cars.general_desription())
print(new_car.get_brand)