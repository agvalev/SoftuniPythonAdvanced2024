def calculate_next_point(command, direction_mapper, current_row_index, current_col_index):
    next_row_index = current_row_index + direction_mapper[command][0]
    next_col_index = current_col_index + direction_mapper[command][1]

    return next_row_index, next_col_index

direction_mapper = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}


n, m = input().split(", ")

n = int(n)
m = int(m)

time_left = 16
defuse_time = 4
matrix = []
counter_terrorist_position = None


for row_index in range(int(n)):
    row_data = list(input())
    if "C" in row_data:
        col_index = row_data.index("C")
        counter_terrorist_position = (row_index, col_index)
        initial_row = row_index
        initial_col = col_index

    elif "B" in row_data:
        col_index = row_data.index("B")
        bomb_position = (row_index, col_index)
    matrix.append(row_data) #provereno do tuk

current_row_index, current_col_index = counter_terrorist_position

initial_row = current_row_index
initial_col = current_col_index

while True:
    if time_left < 0:
        print("Terrorists win!")
        print("Bomb was not defused successfully!")
        print(f"Time needed: {0} second/s.")
        for row in matrix:
            print("".join(row))
        break

    comand = input()

    if comand in ["left", "right", "up", "down"]:
        next_row_index, next_col_index = calculate_next_point(comand, direction_mapper, current_row_index, current_col_index)#provereno do tuk

        if 0 <= next_row_index < n and 0 <= next_col_index < m:
            target_cell = matrix[next_row_index][next_col_index]

            if target_cell == '*':
                current_row_index, current_col_index = next_row_index, next_col_index

            elif target_cell == "T":
                matrix[current_row_index][current_col_index] = "*"
                matrix[next_row_index][next_col_index] = "*"
                print("Terrorists win!")
                for row in matrix:
                    print("".join(row))
                break

            elif target_cell == 'B':
                current_row_index, current_col_index = next_row_index, next_col_index

        time_left -= 1

    elif comand == "defuse":
        if matrix[current_row_index][current_col_index] == "B":
            if time_left >= defuse_time:
                time_left -= defuse_time
                matrix[current_row_index][current_col_index] = "D"
                print("Counter-terrorist wins!")
                print(f"Bomb has been defused: {time_left} second/s remaining.")
                for row in matrix:
                    print("".join(row))
                break

            else:
                matrix[current_row_index][current_col_index] = "X"
                if "C" in matrix:
                    r_index = current_row_index.index("C")
                    c_index = current_col_index.index("C")
                    matrix[r_index][c_index] = "*"

                print("Terrorists win!")
                print("Bomb was not defused successfully!")
                print(f"Time needed: {defuse_time - time_left} second/s.")
                for row in matrix:
                    print("".join(row))
                break
        else:
            time_left -= 2
            continue

