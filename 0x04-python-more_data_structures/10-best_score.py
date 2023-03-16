#!/usr/bin/python3
def best_score(my_dict):
    if my_dict is None or my_dict == {}:
        return None
    max_arr = max(my_dict.values())
    for k, v in my_dict.items():
        if v is max_arr:
            return k
