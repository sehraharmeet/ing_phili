class Car:
    def __init__(self, bd, model, year):
        self.__brand = bd
        self.model = model
        self.year = year
        self.country="Phili"
    def start(self):
        print(f"The {self.__brand} {self.model} starts.")
        print(self.country)

class EV(Car):
    def __init__(self,vt):
        super().__init__("Toyota", "Corolla", 2021)
        self.volt=vt
    def disp(self):
        print(f"Volt {self.volt}")
        

mynewcar=EV(20)
mynewcar.disp()
mynewcar.start()