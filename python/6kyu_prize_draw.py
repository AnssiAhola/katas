from operator import itemgetter

ranks = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
         'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def rank(st, we, n):
    if st == '':
        return "No participants"

    participants = {name: 0 for name in st.split(',')}

    if n > len(participants):
        return "Not enough participants"

    for i, name in enumerate(participants):
        som = len(name)
        for c in name:
            som += ranks.index(c.lower())+1
        participants[name] = som * we[i]

    sorted_by_name = sorted(participants.items(), key=itemgetter(0))
    sorted_by_value = sorted(sorted_by_name, key=itemgetter(1), reverse=True)

    return list(sorted_by_value)[n-1][0]


print(rank("Addison,Jayden,Sofia,Michael,Andrew,Lily,Benjamin",
           [4, 2, 1, 4, 3, 1, 2], 4) == "Benjamin")
print(rank("Lagon,Lily", [1, 5], 2) == "Lagon")
print(rank("Addison,Jayden,Sofia,Michael,Andrew,Lily,Benjamin",
           [4, 2, 1, 4, 3, 1, 2], 8) == "Not enough participants")
print(rank("", [4, 2, 1, 4, 3, 1, 2], 6) == "No participants")
