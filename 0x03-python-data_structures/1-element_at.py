#!/usr/bin/python3


def element_at(my_list, idx):
    num_element = len(my_list) - 1
    if idx < 0 or idx > num_element:
        return None
    return (my_list[idx])
