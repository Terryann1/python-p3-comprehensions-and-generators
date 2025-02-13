#!/usr/bin/env python3

def return_evens(num_list):
    returns_evens = [n for n in num_list if n % 2 == 0]
    return returns_evens
    pass

def make_exclamation(sentence_list):
    
    return [sentence + '!' for sentence in sentence_list]
    pass