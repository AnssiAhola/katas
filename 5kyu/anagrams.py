# https://www.codewars.com/kata/523a86aa4230ebb5420001e1


from timeit import timeit

#length = 6
word = "daring"
#length = 26
words = [
    "dan rig", "dar gin", "dar ing", "dar nig", "darg in", "dig nar", "dig ran", "din gar",
    "din gra", "din rag", "drag in", "gan rid", "gar ind", "gar nid", "garn id", "gid nar",
    "gid ran", "gin rad", "gnar id", "gra ind", "gra nid", "grad in", "id rang", "ind rag",
    "ing rad", "nag rid", "nid rag", "nig rad", "an grid", "an gird", "id gnar", "id garn",
    "and rig", "rad ing", "rad nig", "rad gin", "in drag", "in darg", "in grad", "rag ind",
    "rag nid", "rag din", "gra din", "gar din", "gid arn", "dig arn",
]


# timeit = ~1,5 s
def anagrams(word, words):
    word_sorted = sorted(word)
    words_sorted = [sorted(w) for w in words]
    return [words[i] for i, s in enumerate(words_sorted) if word_sorted == s]


# timeit = ~2.2 s
def anagrams(word, words):
    return [w for w in words if sorted(w) == sorted(word)]


print(timeit(stmt='anagrams(word,words)', number=100000, globals=globals()))

print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) == ['aabb', 'bbaa'])
print(anagrams('racer', ['crazer', 'carer', 'racar',
                         'caers', 'racer']) == ['carer', 'racer'])
print(anagrams('laser', ['lazing', 'lazy', 'lacer']) == [])
