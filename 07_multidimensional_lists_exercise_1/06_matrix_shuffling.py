rows, cols = [int(num) for num in input().split()]

m = [[n for n in input().split()]for i in range(rows)]

commands = ['swap', 'END']

while True:
    user_input = input().split()
    cmd = user_input[0]
    if cmd == "END":
        break
    elif len(user_input) != 5 or cmd not in commands:
        print("Invalid input!")
        continue
    elif cmd == "swap":
        row_1 = int(user_input[1])
        col1 = int(user_input[2])
        row_2 = int(user_input[3])
        col2 = int(user_input[4])
        if 0 <= row_1 < rows and 0 <= row_2 < rows and col1 < cols and col2 < cols:
            m[row_1][col1], m[row_2][col2] = m[row_2][col2], m[row_1][col1]
            for row in m:
                print(' '.join(row))
        else:
            print("Invalid input!")