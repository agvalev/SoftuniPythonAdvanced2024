from python_advanced.python_advanced.advanced_15_modules.ex_4.errors import UknownsignError
def sum(num1, num2):
    return num1+num2

def subtract(num1, num2):
    return num1-num2

def multiply(num1, num2):
    return num1*num2

def divide(num1, num2):
    return num1/num2

def power(num1, num2):
    return num1**num2

mapper = {
    "+": sum,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "^": power
}


def execute(num1, sign, num2):
    if sign in mapper:
        respective_function = mapper[sign]
        return respective_function(num1, num2)
    raise UknownsignError("Please provide a valid sign")