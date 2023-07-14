import random
import string


def generatepassword(passwordlength=8, minupper=1, minlower=1, mindigits=1, minpunct=1):
    """Generate passsword with provided minimum criteria"""

    if passwordlength < 8:
        print("Minimum 8 characters required, updating password length to 8")
        passwordlength = 8
    if minupper < 1:
        print("Atleast one uppercase letter required, updating to 1")
        minupper = 1
    if minlower < 1:
        print("Atleast one lowercase letter required, updating to 1")
        minlower = 1
    if mindigits < 1:
        print("Atleast one digit required, updating to 1")
        mindigits = 1
    if minpunct < 1:
        print("Atleast one special character required, updating to 1")
        minpunct = 1
    rulecharacters = minupper + minlower + mindigits + minpunct
    if rulecharacters > passwordlength:
        passwordlength = rulecharacters
        print("Given password length is shorter than combined length of minimum rule charcters")
        print(f"Password length updated to {passwordlength}")

    password = []
    alphabet = string.ascii_letters + string.digits + string.punctuation
    remaininglength = passwordlength - (minupper + minlower + mindigits + minpunct)

    for _ in range(minupper):
        password.append(random.choice(string.ascii_uppercase))
    for _ in range(minlower):
        password.append(random.choice(string.ascii_lowercase))
    for _ in range(mindigits):
        password.append(random.choice(string.digits))
    for _ in range(minpunct):
        password.append(random.choice(string.punctuation))
    for _ in range(remaininglength):
        password.append(random.choice(alphabet))

    random.shuffle(password)
    passwordstring = "".join(password)
    return passwordstring
