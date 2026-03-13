class Car:
    def __init__(self, brand, model, color, speed):
        self.brand = brand
        self.model = model
        self.color = color
        self.speed = speed

    def car_tuning(self, amount):
        self.speed += amount
        print(f"New speed: {self.speed} km/h")

    def paint_car_with_new_color(self, new_color):
        self.color = new_color
        print(f"New color: {self.color}")

    def print_car(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Color: {self.color}, Speed: {self.speed} km/h")

