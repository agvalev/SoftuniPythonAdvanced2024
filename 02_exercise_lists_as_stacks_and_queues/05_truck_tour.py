from collections import deque

pump_num = int(input())

pumps = deque() # ([1, 5], [10, 20], [7, 3])


for _ in range(pump_num):
    current_fuel, distance = input().split()
    pumps.append([int(current_fuel), int(distance)])

start_position = 0
stops = 0

while stops < pump_num:
    fuel = 0
    for i in range(pump_num):
        fuel += pumps[i][0]
        destination = pumps[i][1]
        if fuel < destination:
            pumps.rotate(-1)
            start_position +=1
            stops = 0
            break
        fuel -= destination
        stops += 1
print(start_position)

