from animal import Animal
from dog import Dog
from cat import Cat
from add_animal import add_animal, list_animals, count_by_species
from shelter import Shelter

# my_animal = Dog("Name: Sakai,", "age 4,", "Specie: Dog", "Breed: Akita")
# my_animal.hours_since_walk = 9
# my_animal.get_info()
# my_animal.make_sound()
# print("Does it need walk?: ",my_animal.needs_walk())
#
# my_animal2 = Cat("Name: Mimi,", "age 3,", "Specie: Cat", True)
# my_animal2.get_info()
# my_animal2.make_sound()
# my_animal2.likes_to_sleep()


shelter = Shelter("Белица")

dog1 = Dog("Sakai", 4, "Dog", "Akita")
dog2 = Dog("Roko", 1, "Dog", "Sheeperd")
cat1 = Cat("Mimi", 3, "Cat", True)
cat2 = Cat("Grozi", 5, "Cat", False)

add_animal(shelter.animals, dog1)
add_animal(shelter.animals, dog2)
add_animal(shelter.animals, cat1)
add_animal(shelter.animals, cat2)

list_animals(shelter.animals)

print(f"Shelter {shelter.name} има {count_by_species(shelter.animals, 'Dog')} кучета.")
dog1.make_sound()
dog1.needs_walk()
dog2.make_sound()
dog2.needs_walk()
cat1.make_sound()
cat1.likes_to_sleep()
cat2.make_sound()
cat2.likes_to_sleep()
