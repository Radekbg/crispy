#Имаш множество от думи. Открий всички групи анаграми (думи с едни и същи букви). 
# Върни множество от кортежи(tuple), където всеки кортеж е група ≥ 2 думи.


words = {"тяло","лотя","котка","тока","акток","тялоо"}

groups = {}
for word in words:
    key = tuple(sorted(word))
    if key not in groups:
        groups[key] = []
    groups[key].append(word)

anagrams = {tuple(sorted(group)) for group in groups.values() if len(group) >= 2}

print(anagrams)


#Резултат: {("тяло","лотя"), ("котка","тока","акток")}