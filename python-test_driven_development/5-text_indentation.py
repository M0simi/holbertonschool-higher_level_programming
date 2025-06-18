#!/usr/bin/python3
def text_indentation(text):
    """
    Prints text with 2 new lines after each '.', '?', and ':'

    Args:
        text (str): The input text.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    split_chars = ['.', '?', ':']
    temp = ""
    for char in text:
        temp += char
        if char in split_chars:
            print(temp.strip())
            print()
            temp = ""
    if temp.strip():
        print(temp.strip())
