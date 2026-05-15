#Имаш списък с рецепти; всяка рецепта има списък с продукти. 
#Състави общ пазарен списък без дублиране на продуктите, за да знаеш какво да напазаруваш без да се повтаряш.

recipe1 = [
    ["яйца", "хляб", "масло"],
    ["спагети", "домат", "масло", "пармезан"],
    ["хляб", "шунка", "кашкавал"]
]

recipe2 = [
    ["Какао", "Сухо Мляко", "масло"],
    ["Бадеми", "Кокос", "Ябълки"],
    ["Брашно", "Лук", "кашкавал"]
]

shopping_list = []
for recipe in recipe1:
    for product in recipe:
        if product not in shopping_list:
            shopping_list.append(product)
            for recipe in recipe2:
                for product in recipe:
                    if product not in shopping_list:
                        shopping_list.append(product)

print(shopping_list)