from math import ceil


class InvalidNumberError(Exception):
    pass


class InvalidValueNumberError(Exception):
    pass


class UnavailablePositionError(Exception):
    pass


def check_position(position, board):
    try:
        position = int(position)
    except ValueError:
        raise InvalidNumberError

    if position < 1 or position > 9:
        raise InvalidNumberError

    selected_row_index = ceil(position / 3) - 1
    selected_col_index = position % 3 - 1

    if board[selected_row_index][selected_col_index] != " ":
        raise UnavailablePositionError

    return position, selected_row_index, selected_col_index


player_one_name = input("Player one name: ")
player_two_name = input("Player two name: ")

while True:
    player_one_sign = input(f"{player_one_name} would you like to play with X or O?").upper()

    if player_one_sign in ("X", "O"):
        break

player_two_sign = "O" if player_one_sign == "X" else "X"

player_one = (player_one_name, player_one_sign)
player_two = (player_two_name, player_two_sign)

num_board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for row in num_board:
    print(f"|  {'  |  '.join([str(el) for el in row])}  |")

board = [[" ", " ", " "] for _ in range(3)]
print(f"{player_one[0]} starts first")
turns = 1
while True:
    current_player = player_one if turns % 2 != 0 else player_two
    position = input(f"{current_player[0]} choose a free position [1-9]: ")

    try:
        position = check_position(position, board)
    except (InvalidNumberError, InvalidValueNumberError, UnavailablePositionError):
        print("Position must be valid number between 1 and 9 including and should be available")
        continue
    else:
        turns += 1
