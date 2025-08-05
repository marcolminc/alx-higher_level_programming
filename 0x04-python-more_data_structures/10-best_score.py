#!/usr/bin/python3
def best_score(a_dictionary):
    high_score, best_key = 0, None
    if a_dictionary:
        for key in a_dictionary:
            if a_dictionary[key] > high_score:
                high_score = a_dictionary[key]
                best_key = key
    return best_key
