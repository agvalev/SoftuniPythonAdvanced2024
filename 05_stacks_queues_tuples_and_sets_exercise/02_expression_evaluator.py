from collections import deque

user_input = input().split()

queue = deque()

for c in user_input:
    if c not in "+-*/":
        queue.append(int(c))
    else:
        while len(queue) > 1:
            num_1 = queue.popleft()
            num_2 = queue.popleft()
            if c == "+":
                queue.appendleft(num_1 + num_2)
            elif c == "-":
                queue.appendleft(num_1 - num_2)
            elif c == "*":
                queue.appendleft(num_1 * num_2)
            elif c == "/":
                queue.appendleft(num_1 // num_2)
print(queue.popleft())


