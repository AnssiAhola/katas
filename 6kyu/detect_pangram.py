# https://www.codewars.com/kata/545cedaa9943f7fe7b000048

import string


def is_pangram(s):
    clean = ''.join([c.lower() if c.isalpha() else '' for c in list(s)])
    return len(set(clean)) == 26

# From kata solutions
def is_pangram(s):
    return set(string.ascii_lowercase) <= set(s.lower())


print(is_pangram("The quick, brown fox jumps over the lazy dog!") == True)
