#!/usr/bin/python3
for letter in range(97, 123):
    print("".join("{}".format(chr(letter)) for letter in range(97, 123) if letter not in (101, 113)), end="")
