import cProfile
from htoa import HashTable


with cProfile.Profile() as pr:
    ht = HashTable(5000)
    COUNT = 5000

    for i in range(COUNT):
        ht.put('key'+str(i), 'val'+str(i))

    for i in range(COUNT):
        ht.get('key'+str(i))

    for i in range(COUNT):
        ht.remove('key'+str(i))

pr.print_stats()
