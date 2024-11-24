from collections import deque

strenght = [int(x)for x in input().split()]
acurracy = deque([int(x)for x in input().split()])

total_goals = 0
while strenght and acurracy:
    cuurent_strenght = strenght[-1]
    current_acuracy = acurracy[0]

    summed_result = cuurent_strenght + current_acuracy

    if summed_result == 100: # goal
        strenght.pop()
        acurracy.popleft()
        total_goals += 1
    elif summed_result < 100:
        if cuurent_strenght < current_acuracy:
            strenght.pop()

        elif cuurent_strenght > current_acuracy:
            acurracy.popleft()

        elif cuurent_strenght == current_acuracy:
            strenght[-1] = summed_result
            acurracy.popleft()

    elif summed_result > 100:
        strenght[-1] -= 10
        popped_acuracy = acurracy.popleft()
        acurracy.append(popped_acuracy)

if total_goals == 3:
    print("Paul scored a hat-trick!")

if total_goals == 0:
    print("Paul failed to score a single goal.")

if total_goals > 3:
    print("Paul performed remarkably well!")

if 0 < total_goals < 3:
    print("Paul failed to make a hat-trick.")

if total_goals > 0:
    print(f"Goals scored: {total_goals}")

if strenght:
    print(f"Strength values left: {', '.join(map(str, strenght))}")

elif acurracy:
    print(f"Accuracy values left: {', '.join(map(str, acurracy))}")
