# https://www.codewars.com/kata/51e04f6b544cf3f6550000c1

def beeramid(bonus, price):
    beercans = int(bonus / price)
    level = 0
    while True:
        beercans_in_next_level = pow(level+1, 2)
        if beercans < beercans_in_next_level:
            return level
        beercans -= beercans_in_next_level
        level += 1


# From kata solutions
def beeramid(bonus, price):
    beers = bonus // price
    levels = 0

    while beers >= (levels + 1) ** 2:
        levels += 1
        beers -= levels ** 2

    return levels


print(beeramid(9, 2) == 1)
print(beeramid(21, 1.5) == 3)
print(beeramid(-1, 4) == 0)
print(beeramid(1500, 2) == 12)
print(beeramid(5000, 3) == 16)
