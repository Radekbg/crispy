#Имаш кортежи с GPS координати на градовете София, Свогер, Лом и Русе. 
# Намери общата „манхатънска“ дължина на маршрута между София и Русе, спирайки във всеки град.

stops = [(0, 0), (2, 3), (2, 7), (5, 7)]

total_distance = 0
for i in range(len(stops) - 1):
    x1, y1 = stops[i]
    x2, y2 = stops[i + 1]
    total_distance += abs(x2 - x1) + abs(y2 - y1)

print(total_distance)