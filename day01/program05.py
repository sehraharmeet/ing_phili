# class Car:
#     def __init__(self, bd, model, year):
#         self.__brand = bd
#         self.model = model
#         self.year = year
#         self.country="Phili"
#     def start(self):
#         print(f"The {self.__brand} {self.model} starts.")
#         print(self.country)

# class EV(Car):
#     def __init__(self,bd, model, year,vt):
#         super().__init__(bd, model, year)
#         self.volt=vt
#     def disp(self):
#         print(f"Volt {self.volt}")
        

# mynewcar=EV("Toyota", "Corolla", 2021,20)
# mynewcar.disp()
# mynewcar.start()

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
    def __init__(self,bd, model, year,vt):
        super().__init__(bd, model, year)
        self.volt=vt
    def disp(self):
        print(f"Volt {self.volt}")
        
class Diesel(Car):
    def __init__(self,bd, model, year,cap):
        super().__init__(bd, model, year)
        self.capacity=cap
    def disp(self):
        print(f"Volt {self.capacity}")
        

mynewcar=EV("Toyota", "Corolla", 2021,20)
mynewcar.disp()
mynewcar.start()

mynewcar2=Diesel("Toyota", "Hillux", 2025,80)
mynewcar2.disp()
mynewcar2.start()