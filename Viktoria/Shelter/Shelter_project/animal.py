class Animal:
    def __init__(self, name, age, species):
        self.name = name
        self.age = age
        self.species = species

    def get_info(self):
        print(self.name, self.age, self.species)

    def make_sound(self):
        print("Some animal sound")