from collections import deque

materials = [int(num) for num in input().split()]
magic = deque([int(num) for num in input().split()])

presents = {}

items = {
    150: 'Doll',
    250: 'Wooden train',
    300: "Teddy bear",
    400: 'Bicycle'
}


while magic and materials:
    current_magic = magic[0] * materials[-1]
    if current_magic in items:
        current_present = items[current_magic]
        if current_present not in presents:
            presents[current_present] = 0
        presents[current_present] += 1
        materials.pop()
        magic.popleft()
    elif current_magic < 0:
        materials.append(magic.popleft() + materials.pop())
    elif current_magic > 0:
        magic.popleft()
        materials[-1] += 15
    else:
        if materials[-1] == 0: materials.pop()
        if magic [0] == 0: magic.popleft()

if ('Doll' in presents and 'Wooden train' in presents) \
        or ('Teddy bear' in presents and 'Bicycle' in presents):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join([str(m) for m in materials[::-1]])}")
if magic:
    print(f"Magic left: {', '.join([str(m) for m in magic])}")
for k, v in sorted(presents.items()):
    print(f"{k}: {v}")











