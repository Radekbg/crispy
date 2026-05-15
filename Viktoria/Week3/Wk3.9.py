#Списък от служители с имейли. Построй речник {} домейн -> списък_служители.

staff = [
  {"name":"Viktoria","email":"viktoria@company.bg"},
  {"name":"Alex","email":"alex@gmail.com"},
  {"name":"Mira","email":"mira@company.bg"},
  {"name":"Radi","email":"georgi@yahoo.com"}
]


by_domain = {}
for person in staff:
    domain = person["email"].split("@")[1]
    if domain not in by_domain:
        by_domain[domain] = []
    by_domain[domain].append(person["name"])

for domain in by_domain:
    by_domain[domain].sort()

print(by_domain)


# Резултат: 
# {
#   "company.bg": ["Mira","Viktoria"],
#   "gmail.com": ["Alex"],
#   "yahoo.com": ["Radi"]
# }

