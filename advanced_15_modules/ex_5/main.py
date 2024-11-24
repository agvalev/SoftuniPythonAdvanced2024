from python_advanced.python_advanced.advanced_15_modules.ex_5.core import create_sequence, locate_index_of_number
data = input()


while data != "Stop":
    seq = None
    if data.startswith("Create"):
        _, _, num = data.split()
        seq = create_sequence(int(num))
        print(*seq)
    else:
        _, num = data.split()
        if seq is not None:
            try:
                index = locate_index_of_number(seq, int(num))
                print(f"The number - {num} is at index {index}")
            except ValueError:
                print(f"The number {num} is not in the sequence")
        else:
            print("Please first create a sequence")




    data = input()