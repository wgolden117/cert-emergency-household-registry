import re

def validate_integer(prompt):
    while True:
        value = input(prompt).strip()
        if value.isdigit():
            return int(value)
        print("Invalid input. Please enter a valid number.")

def validate_yes_no(prompt, optional=False):
    while True:
        value = input(prompt).strip().lower()

        if optional and value == "":
            return None

        if value in ("yes", "no"):
            return value

        print("Invalid input. Please enter 'yes' or 'no'.")

def validate_phone(prompt, optional=False):
    while True:
        value = input(prompt).strip()

        if optional and value == "":
            return None

        if re.fullmatch(r"\d{10}", value.replace("-", "").replace(" ", "")):
            return value

        print("Invalid phone number. Enter 10 digits or leave blank.")

def validate_email(prompt, optional=False):
    while True:
        value = input(prompt).strip()

        if optional and value == "":
            return None

        if re.fullmatch(r"[^@]+@[^@]+\.[^@]+", value):
            return value

        print("Invalid email format. Try again or leave blank.")

def validate_address(prompt):
    while True:
        value = input(prompt).strip()

        # Very basic format check: number + street + commas
        if re.fullmatch(r"\d+ .+, .+, [A-Z]{2} \d{5}", value):
            return value

        print("Invalid address format. Expected: '7001 E Williams Field Rd, Mesa, AZ 85212'")
