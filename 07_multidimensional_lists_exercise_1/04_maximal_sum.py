rows_count, col_count = [int(num) for num in input().split()]

matrix = [[int(num) for num in input().split()]for row in range(rows_count)]

result = -181

max_row_pos = 0
max_col_pos = 0

for row in range(rows_count -2):
    for col in range(col_count -2):
        sum_numbers = 0
        for i in range(row, row + 3):
            for j in range(col, col + 3):
                sum_numbers += matrix[i][j]
        if sum_numbers > result:
            result = sum_numbers
            max_row_pos = row
            max_col_pos = col


print(f"Sum = {result}")

for row in range(max_row_pos, max_row_pos + 3):
    for col in range(max_col_pos, max_col_pos + 3):
        print(matrix[row][col], end=' ')
    print()
