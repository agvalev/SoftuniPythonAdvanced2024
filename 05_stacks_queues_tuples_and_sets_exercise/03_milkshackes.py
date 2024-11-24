from collections import deque

chocolate = [int(num) for num in input().split(", ")]   #stack
milk = deque([int(num) for num in input().split(", ")])   #queue
total = 0

while chocolate and milk and total < 5:

    if chocolate[-1] <= 0 and milk[0] <= 0:
        chocolate.pop()
        milk.popleft()
        continue
    if chocolate[-1] <= 0:
        chocolate.pop()
        continue
    if milk [0] <= 0:
        milk.popleft()
        continue
    if chocolate[-1] == milk[0]:
        total +=1
        chocolate.pop()
        milk.popleft()
    else:
        milk.rotate(-1)
        chocolate[-1] -= 5

if total == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

print(f"Chocolate: {', '.join([str(n) for n in chocolate]) if chocolate else 'empty'}")

print(f"Milk: {', '.join([str(n) for n in milk]) if milk else 'empty'}")


