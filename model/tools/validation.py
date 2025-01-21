import re
from datetime import datetime

def name_family_validation(name, message):
    if type(name) == str and re.match(r"^[a-zA-Z\s]{3,30}$", name):
        return name
    else:
        raise ValueError(message)

def gender_validation(gender):
    genders = ["male", "female", "Male", "Female"]
    if type(gender) == str and gender in genders:
        return gender
    else:
        raise ValueError("Invalid gender")

def number_validation(number):
    if type(number) == int and re.match(r"^[0-9]{9}$", str(number)):
        return number
    else:
        raise ValueError("Invalid Number")

def date_validation(date_input):
    if type(date_input) == str:
        return datetime.strptime(date_input, "%Y-%m-%d").date()
    else:
        raise ValueError("Invalid Date")