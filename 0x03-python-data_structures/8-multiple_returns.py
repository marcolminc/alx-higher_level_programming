#!/usr/bin/python3
def multiple_returns(sentence):
    return tuple((len(sentence), sentence[0] if len(sentence) >= 1 else None))
