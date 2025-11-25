import re

def validate_integer(value):
    value = value.strip()
    if value.isdigit():
        return int(value)
    raise ValueError("Invalid integer")

def validate_yes_no(value, optional=False):
    # Handle None cases first
    if value is None:
        if optional:
            return None
        else:
            raise ValueError("Invalid yes/no")

    # Normalize
    value = value.strip().lower()

    # Optional empty
    if optional and value == "":
        return None

    # Valid values
    if value in ("yes", "no"):
        return value

    raise ValueError("Invalid yes/no")



def validate_phone(value, optional=False):
    value = value.strip()

    if optional and value == "":
        return None

    digits = value.replace("-", "").replace(" ", "")
    if re.fullmatch(r"\d{10}", digits):
        return value

    raise ValueError("Invalid phone number")

def validate_email(value, optional=False):
    value = value.strip()

    if optional and value == "":
        return None

    if re.fullmatch(r"[^@]+@[^@]+\.[^@]+", value):
        return value

    raise ValueError("Invalid email")

def validate_address(value):
    value = value.strip()
    if re.fullmatch(r"\d+ .+, .+, [A-Z]{2} \d{5}", value):
        return value
    raise ValueError("Invalid address format: e.g, 111 street name, city, state zip")

