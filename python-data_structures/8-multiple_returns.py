#!/usr/bin/python3
def multiple_returns(sentence):
    len = len(sentence)
    firstChar = sentence[0] if len < 0 else None
    return (len, firstChar)
