class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


MIN_NAME_LENGTH = 5
TLS_NAMES = [".com", ".bg", ".org", ".net"]
while True:
    user_input = input()
    if user_input == "End":
        break

    if "@" not in user_input:
        raise MustContainAtSymbolError("Email must contain @")

    username, domain = user_input.split("@")

    if len(username) < MIN_NAME_LENGTH:
        raise NameTooShortError("Name must be more than 4 characters")

    _, tls = domain.split(".")
    if f".{tls}" not in TLS_NAMES:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")
    print("Email is valid")
