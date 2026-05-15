#Имаш списък от разходи. Извади само тези, които са над даден праг (threshold), и ги сортирай намаляващо 
# ( може да опиташ без вградена функция, а със selection sort или bubble sort ). 
#След това прецени ще стигне ли заплатата за покриване на всички разходи.

expenses = [12.5, 240, 55.3, 800, 15, 400.2, 75]
threshold = 100
salary = 720
overpriced = []
total = 0

for ammount in expenses:
    total += ammount
    if ammount >= threshold:
        overpriced.append(ammount)
        num_of_elements = len(overpriced)
        for pass_num in range(num_of_elements-1):
            for position in range(num_of_elements - pass_num -1):
                if overpriced[position] > overpriced[position + 1]:
                    overpriced[position], overpriced[position + 1] = overpriced[position + 1], overpriced[position]

overpriced.reverse()
print(overpriced)
print(total)

if total >= salary:
    print("Salary not enough!")
elif total <= salary:
    print("Salary is enough!")