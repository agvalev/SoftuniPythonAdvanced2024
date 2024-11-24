matrix = []

for row in range(3):
    matrix.append([])
    for col in range(1,4):
        matrix[row].append(col)
print(matrix)


matrix = [[] for i in range(3)]
print(matrix)