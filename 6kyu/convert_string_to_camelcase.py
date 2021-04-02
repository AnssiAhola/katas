# https://www.codewars.com/kata/517abf86da9663f1d2000003

def to_camel_case(text):
    output = ''
    flag = 0
    for c in text:
        if c in ['-', '_']:
            flag = 1
        elif flag == 1:
            output += c.upper()
            flag = 0
        else:
            output += c
    return output


print(to_camel_case('') == '')
print(to_camel_case("the_stealth_warrior") == "theStealthWarrior")
print(to_camel_case("The-_Stealth-Warrior") == "TheStealthWarrior")
print(to_camel_case("A-B-C") == "ABC")
