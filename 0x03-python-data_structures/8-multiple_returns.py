#!/usr/bin/python3
def multiple_returns(sentence):
    sen_len = len(sentence)
    f_char = sentence[0] if sen_len > 0 else "None"
    sen_tup = sen_len, f_char
    return(sen_tup)
