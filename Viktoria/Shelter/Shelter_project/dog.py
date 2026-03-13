from animal import Animal

class Dog(Animal):
    def __init__(self, name, age, species, breed):
        super().__init__(name, age, species)
        self.breed = breed
        self.hours_since_walk = 0

    def make_sound(self):
        print("Woof!")

    def needs_walk(self):
        if self.hours_since_walk > 8:
            return True
        else:
            return False

    def get_info(self):
        super().get_info()
        print(self.breed)