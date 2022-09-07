import re


def return_max(value: str):
    numbers = re.findall(r"\d+", re.escape(value))
    return max(numbers)
