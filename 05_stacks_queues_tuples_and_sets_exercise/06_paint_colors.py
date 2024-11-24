from collections import deque

user_input = deque(input().split())
main_colors = ["red", "blue", "yellow", "orange", "purple", "green"]

result = []


def check_color(c, arr):
    if c == "orange" and "red" in arr and "yellow" in arr:
        return True
    elif c == "purple" and "blue" in arr and "red" in arr:
        return True
    elif c == "green" and "blue" in arr and "yellow" in arr:
        return True
    elif c == "red" or c == "blue" or c == "yellow":
        return True
    else:
        return False



while user_input:
    first = user_input.popleft()
    last = user_input.pop() if user_input else ""
    for color in (first + last, last + first):
        if color in main_colors:
            result.append(color)
            break
    else:
        if len(first) > 1:
            user_input.insert(len(user_input) // 2, first[:-1])
        if len(last) > 1:
            user_input.insert(len(user_input) // 2, last[:-1])
for c in result:
    if not check_color(c, result):
        result.remove(c)


print(result)
