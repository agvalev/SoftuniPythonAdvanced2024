presents = int(input())
n = int(input())

matrix = []
santa = []
nice_kids = 0
nice_kids_gifted = 0

for row in range(n):
    matrix.append(input().split())
    for col in range(n):
        if matrix[row][col] == "S":
            santa = [row, col]
        elif matrix[row][col] == "V":
            nice_kids += 1

directions = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}

while presents > 0:
    command = input()
    if command == "Christmas morning":
        break

    r, c = santa[0] + directions[command][0], santa[1] + directions[command][1]
    if 0 <= r < n and 0 <= c < n: #ako r e 0 ili po golqmo i e po malko ot n samo togava vlez
        if matrix[r][c] == "V":
            presents -= 1
            nice_kids_gifted += 1
            matrix[r][c] = "-"
        elif matrix[r][c] == "C":
            for direction in directions.values():
                next_r, next_c = r + direction[0], c + direction[1]
                if matrix[next_r][next_c] in "VX" and presents > 0:
                    presents -= 1
                    if matrix[next_r][next_c] == "V":
                        nice_kids_gifted+=1
                    matrix[next_r][next_c] = "-"
        matrix[santa[0]][santa[1]] = "-"        #tam kudeto e bil santa stava -
        santa = [r, c]      #updatvame kude e v momenta santa v promelivata
        matrix[r][c] = "S"      #updatvame kude e v momenta santa v glavnata matrica

if presents < 1 and nice_kids - nice_kids_gifted > 0 :
    print("Santa ran out of presents!")
for row in matrix:
    print(*row)
if nice_kids - nice_kids_gifted == 0:
    print(f"Good job, Santa! {nice_kids_gifted} happy nice kid/s.")
else:
    print(f"No presents for {nice_kids - nice_kids_gifted} nice kid/s.")

