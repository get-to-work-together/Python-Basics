s = r"""\
Dé plek voor Smart Industry
Brainport Industries Campus is een unieke locatie in de Brainport regio, waar meer dan 50 bedrijven in de hightech maakindustrie en 3 onderwijsinstellingen zijn gevestigd. Smart Industry komt hier letterlijk en figuurlijk van de grond, in een geheel circulair gebouw dat modulair is opgezet.

Een hightech krachtenbundeling
Het is dé plek waar de hightech maakindustrie elkaar ontmoet, waar bedrijven leren van elkaar en direct samenwerken met de nieuwe generatie technisch opgeleiden. Op deze manier wordt er optimaal gebruik gemaakt van kennis en kunde om tot innovatieve oplossingen en vernieuwing te komen.
Behalve kennis en ervaring worden hier ook faciliteiten gedeeld om te produceren en te innoveren. Samen geven we vorm aan het innovatieprogramma Fabriek van de Toekomst voor de high tech maakindustrie.
"""

# clean up

# s = s.lower().replace('.', '').replace(',', '').replace('(', '').replace(')', '')
#
# or
# s = s.lower().translate(str.maketrans('', '', '.,(){}[]/\|#&'))
#
# or

import string
s = s.lower().translate(str.maketrans('é', 'e', string.punctuation))

words = s.split()

unique_words = set(words)

d = dict()
for word in unique_words:
    d[word] = words.count(word)

for word, n in sorted(d.items(), key = lambda item: item[1]):
    print(f'{word:25}: {n:3} {"*" * n}')














# for word, n in sorted(d.items(), key = lambda item: item[1], reverse=True):
#    print(f'{word:20}: {n:3} {"*" * n}')








# # or with a dict comprehension
# d = {word: words.count(word) for word in set(words)}

# for word, n in sorted(d.items()):
#     print(f'{word:20}: {n:3} {"*" * n}')

# from operator import itemgetter
# for word, n in sorted(d.items(), key = itemgetter(1, 0), reverse = True):
#    print(f'{word:20}: {n:3}')

# for word, n in sorted(d.items(), key = lambda item: item[1], reverse=True):
#    print(f'{word:20}: {n:3} {"*" * n}')

# def get_values(item):
#     return item[1]
#
# for word, n in sorted(d.items(), key=get_values, reverse=True):
#     # print(word, n)
#     # print('%-25s: %3d' % (word, n))
#     print(f'{word:<25}: {n:3}')
#     # or
#     print('%-15s: %3d %s' % (word, n, '*' * n))



# # or with collection.Counter
# from collections import Counter
# d = Counter(s.lower().translate(str.maketrans('', '', string.punctuation)).split())
# print(d)
