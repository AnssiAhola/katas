# https://www.codewars.com/kata/513e08acc600c94f01000001

def rgb(r, g, b):
    return "%02X%02X%02X" % tuple(max(0, min(x, 255)) for x in (r, g, b))


print(rgb(0, 0, 0) == "000000")
print(rgb(1, 2, 3) == "010203")
print(rgb(255, 255, 255) == "FFFFFF")
print(rgb(254, 253, 252) == "FEFDFC")
print(rgb(-20, 275, 125) == "00FF7D")
