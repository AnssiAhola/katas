def namelist(names):
    l = len(names)
    if l == 0:
        return ''
    if l == 1:
        return names[0]['name']
    output = ', '.join(item['name'] for item in names[:-1])
    return ' & '.join((output, names[-1]['name']))


print(namelist([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}, {
      'name': 'Homer'}, {'name': 'Marge'}]) == 'Bart, Lisa, Maggie, Homer & Marge')
print(namelist([{'name': 'Bart'}, {'name': 'Lisa'},
                {'name': 'Maggie'}]) == 'Bart, Lisa & Maggie')
print(namelist([{'name': 'Bart'}, {'name': 'Lisa'}]) == 'Bart & Lisa')
print(namelist([{'name': 'Bart'}]) == 'Bart')
print(namelist([]) == '')
