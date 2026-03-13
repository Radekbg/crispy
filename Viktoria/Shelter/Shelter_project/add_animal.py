from animal import Animal
from dog import Dog
from cat import Cat

def add_animal(animals_list, animal):
    if not isinstance(animal, Animal):
        print("Грешка: обектът не е животно!")
        return
    if not isinstance(animal, (Dog, Cat)):
        print("Грешка: можем да приемем само кучета или котки!")
        return
    animals_list.append(animal)
    print(f"{animal.name} е добавен в приюта.")

def list_animals(animals_list):
    for animal in animals_list:
        animal.get_info()

def count_by_species(animals_list, species):
    count = 0
    for animal in animals_list:
        if animal.species == species:
            count += 1
    return count




