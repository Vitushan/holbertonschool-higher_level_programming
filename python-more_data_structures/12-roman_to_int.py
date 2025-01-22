#!/usr/bin/python3
def roman_to_int(roman_string):
    """Convert a Roman numeral string to an integer."""
    if not roman_string or not isinstance(roman_string, str):
        return 0

    romane_value = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    total = 0

    for i in range(len(roman_string)):
        current_value = romane_value.get(roman_string[i])
        if current_value is None:
            return 0
        if i + 1 < len(roman_string) and romane_value[roman_string[i + 1]] > current_value:
            total -= current_value
        else:
            total += current_value

    return total
