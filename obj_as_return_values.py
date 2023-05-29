class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

def build_car(make, model, year):
    new_car = Car(make, model, year)
    return new_car

my_car = build_car("Toyota", "Camry", 2020)
print(my_car.make)   # Output: Toyota
print(my_car.model)  # Output: Camry
print(my_car.year)   # Output: 2020


'''This example demonstrates how returning instances of classes as return values in Python can be useful
for creating and modifying objects within functions, and then using those modified objects outside of 
the function.'''