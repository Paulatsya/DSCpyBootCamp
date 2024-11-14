# Define the Car class
class Car:
    def __init__(self, brand, color):
        self.brand = brand        # attribute: the brand of the car
        self.color = color        # attribute: the color of the car

    # Method to start the car
    def start(self):
        print(f"The {self.color} {self.brand} car is now starting.")

# Usage example
my_car = Car("Toyota", "red")

# Starting the car
my_car.start()
