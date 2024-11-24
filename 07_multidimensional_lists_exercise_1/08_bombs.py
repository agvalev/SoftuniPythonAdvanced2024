m_size = int(input())
m = []
for _ in range(m_size):
    current_row = [int(n) for n in input().split()]
    m.append(current_row)

bombs = input().split()

def get_cells(x, y, s):
    cells = []
    if x - 1 in range(s) and y-1 in range(s):
        cells.append((x - 1, y-1))

    if x in range(s) and y - 1 in range(s):
        cells.append((x, y - 1))

    if x +1 in range(s) and y - 1 in range(s):
        cells.append((x + 1, y - 1))

    if x -1 in range(s) and y in range(s):
         cells.append((x - 1, y))

    if x+1 in range(s) and y in range(s):
        cells.append((x+1, y))

    if x-1 in range(s) and y +1 in range(s):
        cells.append((x - 1, y + 1))

    if x in range(s) and y + 1 in range(s):
        cells.append((x, y + 1))

    if x + 1  in range(s) and y + 1 in range(s):
        cells.append((x + 1, y + 1))

    return cells

for bomb in bombs:
    row, col = [int(n) for n in bomb.split(',')]
    current_bomb = m[row][col]
    if current_bomb > 0:
        neighbour_cells = get_cells(row, col ,m_size)
        for r, c in neighbour_cells:
            if m[r][c] > 0:
                m[r][c] -= current_bomb
        m[row][col] = 0
result_count = 0
result_sum = 0

for row in range(m_size):
    for col in range(m_size):
        if m[row][col] > 0:
            result_count += 1
            result_sum += m[row][col]
print(f"Alive cells: {result_count}")
print(f"Sum: {result_sum}")

for row in range(m_size):
    print(*m[row])

