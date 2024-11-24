with open("my_first_file.txt", "a") as file:
    for _ in range(3):
        file.write("i just created my first file!\n")
    