matrix = [[1, 2, 3], [4, 5, 6]]

result = []

for row_data in matrix:
    for el in row_data:
        result.append(el)
print(result)

flattened = [num for sublist in matrix for num in sublist]
print(flattened)