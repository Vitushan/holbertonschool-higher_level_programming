#!/usr/bin/python3
def text_indentation(text):
    """
    Function that prints a text with two new lines after each of these characters: ., ? and :
    
    Args:
        text (str): The string to print and modify.
    
    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    while i < len(text):
        print(text[i], end="")

        # Check for the punctuation marks and print a new line after them
        if text[i] in ['.', '?', ':']:
            print("\n")
            # Skip any spaces after the punctuation
            while i + 1 < len(text) and text[i + 1] == " ":
                i += 1

        i += 1
