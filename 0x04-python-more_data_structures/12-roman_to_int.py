#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or not roman_string:
        return 0
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                  'C': 100, 'D': 500, 'M': 1000}
    prev = 0
    result = 0
    for symbol in reversed(roman_string):
        nxt = roman_dict.get(symbol, 0)
        if nxt < prev:
            result -= nxt
        else:
            result += nxt
        prev = nxt
    return result
