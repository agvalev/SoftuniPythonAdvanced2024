numbers = input().split()

stack = []

# for i in range(len(numbers)):
#     stack.append(numbers.pop()) 2ri nachin da q reshim(po slojen)
while numbers:
    stack.append(numbers.pop())

print(" ".join(stack))