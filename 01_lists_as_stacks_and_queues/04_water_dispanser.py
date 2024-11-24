from collections import deque
avb_liters = int(input())

name = input()
custumurs = deque()

while name != "Start":
    custumurs.append(name)
    name = input()

command = input()

while command != "End":
    if command.isdigit():
        custumur = custumurs.popleft()
        liters_wanted = int(command)
        if liters_wanted <= avb_liters:
            avb_liters -= liters_wanted
            print(f"{custumur} got water")
        else:
            print(f"{custumur} must wait")

    else:
        refill_command, liters = command.split()
        liters = int(liters)
        avb_liters += liters
    command = input()

print(f"{avb_liters} liters left")