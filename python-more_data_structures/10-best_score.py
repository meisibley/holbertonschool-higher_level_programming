#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        bscore = 0
        for x, y in a_dictionary.items():
            if y > bscore:
                bscore = y
                bkey = x
        return bkey
    else:
        return None
