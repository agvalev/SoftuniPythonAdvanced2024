rows, cols = [int(num) for num in input().split()]


for r in range(rows):
    for c in range(cols):
        print(f"{chr(97 + r)}{chr(97 + r + c)}{chr(97 + r)}", end=' ')
    print()