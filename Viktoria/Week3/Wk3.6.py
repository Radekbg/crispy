#Имаш списък с имейл адреси, до които са пращани имейли през последния месец, Хрис ги е събрал но някои са дублирани.
# Върни списък с имейли без дубликати, за да създадеш distribution list на екипа.

emails = ["a@x.com","b@x.com","a@x.com","c@x.com","b@x.com","d@x.com"]

unique = []

for i in emails:
    count = 0
    for j in unique:
        if j == i:
            count += 1
    if count == 0:
        unique.append(i)

print(unique)


#Резултат: ["a@x.com", "b@x.com", "c@x.com", "d@x.com"]
