n = int(input())

matrix = [[int(x)for x in input().split()]for _ in range(n)]


while True:
    line = input().split()
    if line[0] == "END":
        break
    command = line[0]

    row, col, value = map(int, line[1:])
    if row < 0  or row >= n or col < 0  or col >= n:
        print("Invalid coordinates")
        continue

    if command == "Add":
        matrix[row][col] += value

    elif command == "Subtract":
        matrix[row][col] -= value

[print(*row)for row in matrix]