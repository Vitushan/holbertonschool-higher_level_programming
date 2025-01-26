#!/usr/bin/python3
def text_indentation(text):
    """
    Function that prints a text with two new lines after each of these characters: ., ? and :
    Args: text (str): The string to print and modify.
    Raises: TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    while i < len(text):
        # Print the character without adding a space after it
        print(text[i], end="")

        # If we encounter a punctuation mark, print two new lines
        if text[i] in ['.', '?', ':']:
            print("\n")  # Add the first new line
            # Skip any spaces following the punctuation
            while i + 1 < len(text) and text[i + 1] == " ":
                i += 1
            print()  # Add the second new line
        
        i += 1
