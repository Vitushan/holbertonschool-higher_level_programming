#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        print("Error: 🚫 is empty or not a string.")
        return 0

    roman_number = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    total = 0

    for i in range(len(roman_string)):
        current_value = roman_number.get(roman_string[i])

        if current_value is None:
            print(f"Error: 🚫 {roman_string[i]} is not a valid Roman number.")
            return 0

        if i + 1 < len(roman_string):
            next_value = roman_number[roman_string[i + 1]]
            if current_value < next_value:
                total -= current_value
            else:
                total += current_value
        else:
            total += current_value
    return total

if __name__ == "__main__":
    roman_str = input("\tEnter a Roman Number: ")
    roman_str = roman_str.upper()
    print(f"Roman Number: {roman_str} || Arabic Number: {roman_to_int(roman_str)}")
