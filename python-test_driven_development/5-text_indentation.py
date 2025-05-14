#!/usr/bin/python3
def text_indentation(text):
    """Prints a text with 2 new lines after each '.', '?', and ':'"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    current = ""
    for char in text:
        current += char
        if char in ".:?":
            print(current.strip())
            print()
            current = ""
    if current.strip():
        print(current.strip(), end="")
