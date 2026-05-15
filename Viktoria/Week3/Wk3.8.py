#Имаш списък от записи (категория, сума) за разходи. Направи речник (dictionary) категория -> обща_сума

expenses = [
  ("Храна", 24.5), ("Транспорт", 3.2), ("Храна", 10),
  ("Наем", 500), ("Комунални", 120), ("Храна", 30), ("Транспорт", 25)
]


totals = {}
for category, amount in expenses:       #Unpacking, working with tuples with only 2 elements
    if category not in totals:
        totals[category] = 0
    totals[category] += amount

print(totals)

#Резултат: [("Наем", 500), ("Храна", 64.5), ("Комунални", 120) .......]

#Alternative solution without unpacking
# totals = {}

# for item in expenses:
#     category = item[0]
#     amount = item[1]

#     if category not in totals:
#         totals[category] = 0

#     totals[category] += amount

# print(totals)