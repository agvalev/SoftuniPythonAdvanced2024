from functools import reduce


def operate(operator, *args):

    def sum_nums():
        return reduce(lambda x, y: x + y, args)

    def subtract_nums():
        return reduce(lambda x, y: x - y, args)

    def multiply_nums():
        return reduce(lambda x, y: x * y, args)

    def divide_nums():
        return reduce(lambda x, y: x / y, args)

    if operator == "+":
        return sum_nums()

    elif operator == "-":
        return subtract_nums()

    elif operator == "*":
        return multiply_nums()

    elif operator == "/":
        return divide_nums()


print(operate("*", 1, 2, 3))
