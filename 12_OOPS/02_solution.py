class Cars:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    def fullName(self):
        return f"{self.brand} {self.model}"

class ElectricCar(Cars):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.batterySize = battery_size
    
    def fullStats(self):
        return f"{self.model} by {self.brand} have battery size of {self.batterySize}"


ev_car = ElectricCar("Tesla","S Model","100KWH")
print(ev_car.model)
print(ev_car.fullName())
print(ev_car.fullStats())