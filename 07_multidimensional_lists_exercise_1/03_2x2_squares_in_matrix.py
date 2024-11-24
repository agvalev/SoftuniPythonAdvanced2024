rows_count, col_count = [int(num) for num in input().split()]

matrix = [[c for c in input().split()] for row in range(rows_count)]

result = 0
for row in range(rows_count - 1):
    for col in range(col_count - 1):
        char_1 = matrix[row][col]
        char_2 = matrix[row][col + 1]
        char_3 = matrix[row + 1][col]
        char_4 = matrix[row + 1][col + 1]
        if char_1 == char_2 == char_3 == char_4:
            result += 1
print(result)
