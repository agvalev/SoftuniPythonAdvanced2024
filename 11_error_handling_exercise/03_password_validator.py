class PasswordTooShortError(Exception):
    pass


class PasswordTooCommonError(Exception):
    pass


class PasswordNoSpecialCharactersError(Exception):
    pass


class PasswordContainsSpacesError(Exception):
    pass

PASSWORD_MIN_LENGTH = 8
SPECIAL_CHARACTERS = ("@", "*", "&", "%")

while True:
    pwd = input()
    if pwd == "Done":
        break
    if len(pwd) < PASSWORD_MIN_LENGTH:
        raise PasswordTooShortError("Password must contain at least 8 characters")
    if pwd.isalpha() or pwd.isdigit() or all(c in SPECIAL_CHARACTERS for c in pwd):
        raise PasswordTooCommonError("Password must be a combination of digits, letters, and special characters")
    if not any(c in SPECIAL_CHARACTERS for c in pwd): #za vseki edin simvol v nashata parola ako edin e vuv special ch vrushta true/ a all e ako vsichkite sa vuv special ch
        raise PasswordNoSpecialCharactersError("Password must contain at least 1 special character")
    if ' ' in pwd:
        raise PasswordContainsSpacesError("Password must not contain empty spaces")
    print("Password is valid")