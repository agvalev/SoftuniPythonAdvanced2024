row_count, col_count = [int(el) for el in input().split(", ")]

matrix = []
elements_sum = 0
for row in range(row_count):
    row_data = [int(el) for el in input().split(", ")]
    elements_sum += sum(row_data)
    matrix.append(row_data)

print(elements_sum)
print(matrix)

