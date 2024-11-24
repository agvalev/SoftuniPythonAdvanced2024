matrix = [[int(num) for num in input().split(", ")] for row in range(int(input()))]


left = []
right = []


for i, j in zip(range(0, len(matrix)), range(len(matrix) -1, -1, -1)):
    a = matrix[i][i]
    b = matrix[i][j]
    left.append(a)
    right.append(b)

print(f"Primary diagonal: {', '.join(str(num) for num in left)}. Sum: {sum(left)}")
print(f"Secondary diagonal: {', '.join(str(num) for num in right)}. Sum: {sum(right)}")
