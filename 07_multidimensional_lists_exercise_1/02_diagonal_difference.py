matrix = [[int(num) for num in input().split()] for row in range(int(input()))]

left = 0
right = 0

for i, j in zip(range(0, len(matrix)), range(len(matrix) - 1, -1, -1)):
    a = matrix[i][i]
    b = matrix[i][j]
    left += a
    right += b

print(abs(left - right))
