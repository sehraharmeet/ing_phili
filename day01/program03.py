class Car:
    def __init__(self, bd, model, year):
        self.__brand = bd
        self.model = model
        self.year = year
        self.country="Phili"
    def start(self):
        print(f"The {self.__brand} {self.model} starts.")
        print(self.country)

# Creating an object
my_car = Car("Toyota", "Corolla", 2021)
my_car.start()  # Output: The Toyota Corolla starts.
print(my_car.__brand)
