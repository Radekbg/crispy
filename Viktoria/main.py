from car import Car
from garage import Garage

# car1 = Car("Red","210", "Trabant")
# car1.carPrint()

my_car = Car("BMW", "M3", "Red", 250)
my_car2 = Car("Suzuki", "Liana", "Dark Grey", 200)
my_car3 = Car("Ford", "F-150", "Blue", 200 )
my_car4 = Car("Ferrari", "Speciale", "Red", 350)

# my_car.printCar()
# my_car.carTuning(30)
# my_car.paintCarWithNewColor("Blue")
# my_car.printCar()

my_garage = Garage("str. Aleksi Rilec", [my_car, my_car2, my_car3, my_car4])
my_garage.list_cars()

my_car.paint_car_with_new_color("Blue")
my_garage.list_cars()

new_garage = Garage("str.Georgi Rusev", [my_car, my_car2, my_car3, my_car4])
new_garage.fastest_car()