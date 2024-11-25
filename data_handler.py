import re
import html
import urllib.parse
import bcrypt  # to be used later


def password_data_handling(password: str) -> bool:
    if len(password) < 9 or len(password) > 12:
        return False
    alphacount = 0
    numcount = 0
    symbolcount = 0
    for c in password:
        if c.isalpha():
            alphacount += 1
        elif c.isdigit():
            numcount += 1
        elif c.isascii() and not c.isalnum():
            symbolcount += 1
        else:
            return False
    if alphacount < 4 or numcount < 3 or symbolcount < 2:
        return False
    return True


# def example_password_data_handling(password: str) -> bool:
#     pattern = r'^(?=.*[A-Za-z]{4,})(?=.*\d{3,})(?=.*[!@#$%^&*()_+{}\[\]:;"\'<>,.?/~`-]{2,}).{9,12}$'
#     return bool(re.match(pattern, password))


def feedback_data_handling(feedback: str) -> str:
    return urllib.parse.quote(feedback, safe=" ")


if __name__ == "__main__":
    test = input("Enter feedback: ")
    print(feedback_data_handling(test))
