n = int(input())

matrix = []
for i in range(n):
    row_data = list(input())
    matrix.append(row_data)

searched_symbol = input()

position = None

for row_index in range(n):
    for column_index in range(n):
        if matrix[row_index][column_index] ==  searched_symbol:
            position = f"({row_index}, {column_index})"
            print(position)
            exit()


print(f"{searched_symbol} does not occur in the matrix")

