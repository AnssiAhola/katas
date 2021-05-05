# https://www.codewars.com/kata/530e15517bc88ac656000716


def rot13(message):
    output = ''

    for c in message:
        if not c.isalpha():
            output += c
            continue

        # Nth alphabet (lowercase)
        alphabet_n = ord(c.lower()) - ord('a')
        # == 26
        alphabet_count = ord('z') - ord('a') + 1
        # add rot
        rot = (alphabet_n + 13) % alphabet_count
        # get rotted alphabet
        char = chr(rot + ord('a'))
        # apply original letter case
        output += char if c.islower() else char.upper()

    return output


print(rot13("test") == "grfg")
print(rot13("Test") == "Grfg")
