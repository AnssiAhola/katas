def is_pangram(s):
    clean = ''.join([c.lower() if c.isalpha() else '' for c in list(s)])
    return len(set(clean)) == 26


print(is_pangram("The quick, brown fox jumps over the lazy dog!"), True)
