# https://www.codewars.com/kata/58ad317d1541651a740000c5

# From kata solutions
def middle_permutation(string):
    s = sorted(string)
    n = len(s)
    if n % 2 == 0:
        return s.pop(n//2-1) + ''.join(s[::-1])
    else:
        return s.pop(n//2) + middle_permutation(s)


print(middle_permutation("abc") == "bac")
print(middle_permutation("abcd") == "bdca")
print(middle_permutation("abcdx") == "cbxda")
print(middle_permutation("abcdxg") == "cxgdba")
print(middle_permutation("abcdxgz") == "dczxgba")
