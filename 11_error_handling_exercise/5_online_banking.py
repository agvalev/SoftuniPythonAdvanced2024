class MoneyNotEnoughError(Exception):
    pass


class PINCodeError(Exception):
    pass


class UnderageTransactionError(Exception):
    pass


class MoneyIsNegativeError(Exception):
    pass


user_input = input().split(", ")
user_pin = user_input[0]
user_balance = int(user_input[1])
user_age = int(user_input[2])

LEGAL_AGE = 18
while True:
    user_input = input().split("#")
    cmd = user_input[0]
    if cmd == 'End':
        break
    if cmd == "Send Money":
        amount = int(user_input[1])
        pin = user_input[2]
        if user_balance < amount:
            raise MoneyNotEnoughError("Insufficient funds for the requested transaction")
        if pin != user_pin:
            raise PINCodeError("Invalid PIN code")
        if user_age< LEGAL_AGE:
            raise UnderageTransactionError("You must be 18 years or older to perform online transactions")
        user_balance -= amount
        print(f"Successfully sent {amount:.2f} money to a friend")
        print(f"There is {user_balance:.2f} money left in the bank account")
    if cmd == "Receive Money":
        amount = int(user_input[1])
        if amount < 0:
            raise MoneyIsNegativeError("The amount of money cannot be a negative number")
        user_balance += amount / 2
        print(f"{amount / 2:.2f} money went straight into the bank account")




