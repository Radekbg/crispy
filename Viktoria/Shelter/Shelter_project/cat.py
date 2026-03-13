from animal import Animal

class Cat(Animal):
    def __init__(self, name, age, species, is_indoor):
        super().__init__(name, age, species)
        self.is_indoor = is_indoor

    def get_info(self):
        print(f"{self.name} {self.age} {self.species} \nIs it indoor?: {self.is_indoor}")

    def make_sound(self):
        print("Meow!")

    def likes_to_sleep(self):
        print("Sleeps all day")