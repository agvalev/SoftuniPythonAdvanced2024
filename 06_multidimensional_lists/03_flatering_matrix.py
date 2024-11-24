n = int(input())

matrix = []
flat_result = []

for i in range(n):
    row_data = [int(el) for el in input().split(", ")]
    matrix.append(row_data)
    # flat_result.extend(row_data) # sus tova moje da go flatvash bez 2 for cikula!!!

# print(flat_result)


for row in matrix:
    for el in row:
        flat_result.append(el)
print(flat_result)





# flat_result = [el for row in matrix for el in row] # kogato chetem matrica golemiqt for cikul e ot dqsno
# print(flat_result)