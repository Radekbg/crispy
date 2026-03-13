class Garage:
    def __init__(self, street, brands):
        self.street = street
        self.brands = brands

    def list_cars(self):
        print("Car brands:")
        for car in self.brands:
            car.print_car()

    def fastest_car(self):
        fastest = self.brands[0]

        for car in self.brands:
            if car.speed > fastest.speed:
                fastest = car

        print("Fastest car:")
        fastest.print_car()