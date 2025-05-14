#!/usr/bin/python3
def text_indentation(text):
    """
    Prints a text with 2 new lines after each '.', '?'
    and ':'
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    line = ""
    for char in text:
        if char in ".:?":
            line += char
            print(line.strip())
            print()
            line=  ""
        else:
            line += char
    if line.strip():
        print(line.strip(), end="")
