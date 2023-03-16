#!/usr/bin/python3
def complex_delete(my_dict, value):
    arr = []
    for key, key_value in my_dict.items():
        if key_value is value:
            arr.append(key)
    for x in arr:
        del my_dict[x]
    return(my_dict)
